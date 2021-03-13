import logging
from datetime import date
import gspread_asyncio
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
import discord

from src.configs import TOKEN
from src.messages import createEmbed

bot = commands.Bot(command_prefix='!')
logging.basicConfig(filename='praise.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


def get_creds():
    # To obtain a service account JSON file, follow these steps:
    # https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account
    return ServiceAccountCredentials.from_json_keyfile_name(
        "src/admin_creds.json",
        [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/spreadsheets",
        ],
    )


agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)


# Upload data to spreadsheet
async def upload_praise(agcm, praise_to, praise_from, reason, date, server, chat):
    agc = await agcm.authorize()

    ss = await agc.open("Discord Praise Bot Sheet")
    print("Spreadsheet URL: https://docs.google.com/spreadsheets/d/{0}".format(ss.id))
    zero_ws = await ss.get_worksheet(0)
    await zero_ws.append_row([praise_to, praise_from, reason, server, date, chat])


# Parse the reason of praise
async def praise_for(data, mentions):
    users = []
    for i in mentions:
        user = '@' + i.name
        users.append(user)
    praise_for = ""
    for i in data:
        if i in users:
            continue
        praise_for += i + ' '
    return praise_for


# Parse praised persons
async def parse_persons(mentions):
    persons = {}
    for i in mentions:
        person = "@" + i.name + '#' + i.discriminator
        persons[i.id] = person
    return persons


async def send_notification(server_id, users, message_link):
    for user in users:
        logging.info('Trying to send notification to userId:{}, server:{}'.format(user.id, server_id))

        try:
            message_data = createEmbed(server_id, message_link)
            await user.send(embed=message_data['embed'], file=message_data['file'])
            logging.info('DM notification sended to userId:{}, server:{}'.format(user.id, server_id))
        except Exception as e:
            if e.code == 50007:
                continue
            else:
                logging.error('Failed to send notification. Exception:{}'.format(e))
                return False
    return True


@commands.has_any_role('Praise Giver')
@bot.command(name='praise_log')
async def log(ctx):
    user = bot.get_user(ctx.message.author.id)
    with open("praise.log", "rb") as file:
        await user.send("Praise log is:", file=discord.File(file, "praise_log.txt"))


@commands.has_any_role('Praise Giver')
@bot.command(name='praise')
async def send(ctx, *content: commands.clean_content(use_nicknames=False)):
    author = '@' + ctx.message.author.name + '#' + ctx.message.author.discriminator
    server = ctx.message.guild.name
    server_id = ctx.message.guild.id
    message_link = ctx.message.jump_url
    channel = ctx.message.channel.name
    now = date.today().strftime("%b-%d-%Y")

    logging.info('Trying to dish Praise. admin={}, server={}, channel={}'.format(author, server, channel))
    if not (persons := await parse_persons(ctx.message.mentions)):
        logging.warning('Users not specified')
        await ctx.send(ctx.message.author.mention + " Specify the user")
        return

    logging.info('Users found. users: {}'.format(persons))
    if not (reason := await praise_for(content, ctx.message.mentions)):
        logging.warning('Reason not specified')
        await ctx.send(ctx.message.author.mention + " Specify the reason")
        return
    logging.info('Reason found. reason: {}'.format(reason))

    status = True
    users = []
    for user_id, username in persons.items():
        try:
            logging.info('Trying to upload praise data. User={}, reason={}, server={}, channel={}, admin={}'.format(
                username, reason, server, channel, author))
            await upload_praise(agcm, username, author, reason, now, server, channel)
            logging.info('Praise data uploaded for user={}'.format(username))
            users.append(bot.get_user(user_id))
        except Exception as e:
            logging.warning('Failed to upload Praise data for user={}. Exception:{}'.format(username, e))
            status = False

    if not await send_notification(server_id, users, message_link):
        status = False

    if status:
        logging.info('Admin {} successfully praised users [{}]'.format(author, persons))
        await ctx.message.add_reaction('✅')
    else:
        logging.warning('The admin {} failed to praise one or more users. Users [{}]'.format(author, persons))
        await ctx.message.add_reaction('⚠️')


bot.run(TOKEN)
