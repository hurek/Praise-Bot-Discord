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
        await ctx.send(f'Fetching all Praise from {ctx.guild.name}...')

        if after:
            dates = [int(char) for char in after.split('-')]
            after = datetime(dates[2], dates[1], dates[0])
        else:
            # praise from server creation date
            after=ctx.guild.created_at

        clean_msgs = [["To", "From", "Reason for Dishing", "Date", "Server", "Room"]]
        msg_logs = OrderedDict()
        praise_duration = f"from {after.strftime('%b-%d-%Y')}"

        await ctx.send(f"Attempting to get praise {praise_duration}")
        for channel in ctx.guild.text_channels:
            await sleep(5)
            try:
                log.info(f"Attempting to get praise in {channel.name} {praise_duration}")
                await ctx.send("Attemting to get praise in {channel.name}")

                async for msg in channel.hostory(after=after, limit=None):
                    if msg.content.startswith('!praise'):
                        for person in msg.mentions:
                            timestamp = msg.created_at.strftime("%b-%d-%Y")
                            info = [
                                person.name + "#" + person.discriminator,
                                msg.author.name + "#" + msg.author.discriminator,
                                re.sub(r'(<@).*?>', '', utils.escape_mentions(msg.content)[8:]).strip().replace('\n', ' '),
                                msg.created_at.strftime("%b-%d-%Y"),
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

        for msg_log in msg_logs.values():
            for msg_data in msg_log:
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
