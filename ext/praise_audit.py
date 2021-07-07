import re
import csv
import logging

from asyncio import sleep
from datetime import datetime, timedelta
from collections import OrderedDict

from discord import utils, File
from discord.ext import commands
from discord.ext.commands import Context
from discord.errors import Forbidden, HTTPException


log = logging.getLogger(__name__)

class PraiseAudit(commands.Cog):
    """Commands for scraping old praise from the server"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def praise_audit(self, ctx: Context, after: str = None):
        await ctx.send(f'Fetching all the Praise from {ctx.guild.name} for the Audit...')

        if after:
            dates = [int(char) for char in after.split('-')]
            after = datetime(dates[2], dates[1], dates[0])
        else:
            # praise from server creation date
            after=ctx.guild.created_at

        clean_msgs = [["To", "From", "Reason for Dishing", "Date", "Server", "Room"]]
        msg_logs = dict()
        praise_duration = f"from {after.strftime('%b-%d-%Y')}"
        # Ignore these channels, to reduce API calls
        # TODO: Re-implement this list to be more DRY, and be located in a config file
        skip_channels = [
            810183289863798815, # join-here (TEC)
            831938823172653076, # announcements (TEC)
            810180622336262197, # tec-tokenholders
            810180622966325296, # ECOSYSTEM
            810180622966325291, # ECOSYSTEM
            810180622966325292, # ECOSYSTEM
            810180622966325293, # ECOSYSTEM
            810180622966325294, # ECOSYSTEM
            810180622966325295, # ECOSYSTEM
            857623810455109692, # ECOSYSTEM
            778081852492873758, # rules (CS)
            780557396778549330, # announcements (CS)
            824917827831595028, # claim-a-role (CS)
            778081852492873759, # moderator-only (CS)
            778085977125158922, # system-messages (CS)
            801882792942239818  # praise-testing (CS)
        ]

        await ctx.send(f"Attempting to get praise {praise_duration}")
        for channel in ctx.guild.text_channels:

            await sleep(5)

            try:
                if channel.id in skip_channels:
                    await ctx.send(f"Skipping {channel.name}")
                    log.info(f"Skipping {channel.name} from praise-audit")
                else:
                    await ctx.send(f"Attempting to get praise in {channel.name}")
                    log.info(f"Attempting to get praise in {channel.name} {praise_duration}")

                async for msg in channel.history(after=after, limit=None):
                    if msg.content.startswith('!praise'):
                        for person in msg.mentions:
                            timestamp = msg.created_at.strftime("%b-%d-%Y")
                            info = [
                                person.name + "#" + person.discriminator,
                                msg.author.name + "#" + msg.author.discriminator,
                                re.sub(r'(<@).*?>', '', utils.escape_mentions(msg.content)[8:]).strip().replace('\n', ' '),
                                timestamp,
                                msg.guild.name,
                                msg.channel.name
                            ]
                            if timestamp not in msg_logs:
                                msg_logs[timestamp] = []

                            msg_logs[timestamp].append(info)
                            log.info(f'Adding praise for: {person.name} - {msg.channel.name}')
            except Forbidden:
                log.error(f"Missing perms... Skipping praise scraping from channel - {channel.name}")
                continue
            else:
                continue

        for date in sorted(msg_logs.keys(), key=lambda x: datetime.strptime(x, '%b-%d-%Y')):
            for msg_data in msg_logs[date]:
                clean_msgs.append(msg_data)

        with open(f"praise_audit_{ctx.guild.id}.csv", 'w') as f:
            try:
                writer = csv.writer(f)
                log.info('Writing Praise...')
                writer.writerows(clean_msgs)
            except Exception as e:
                log.error(f"Error in writing Praise: {e}")

            log.info("Praise successfully written!")
        await ctx.send("Praise collected and written!")
        await ctx.send(
            f"Praise written! Here's all of the Praise in the server for the audit",
            file = File(f'praise_audit_{ctx.guild.id}.csv', f'{ctx.guild.name} praise.csv')
        )
    @praise_audit.error
    async def get_praise_error(self, ctx: Context, error):
        if isinstance(error.original, HTTPException):
            await ctx.send("An error occured, the date format might be wrong.")
        log.error(f"An error occured\n{error}")

def setup(bot):
    bot.add_cog(PraiseAudit(bot))
