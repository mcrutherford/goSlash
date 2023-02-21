"""
File: goSlash.py
Author: Mark Rutherford
Created: 02/21/2023 2:30 PM
"""
import re
import threading

import discord
from discord.ext import commands


class GoSlash(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.lock = threading.Lock()

    @commands.Cog.listener("on_message")
    async def on_message(self, message: discord.Message):
        # Ignore messages from itself
        if message.author == self.bot.user:
            return

        # Check if the expenses were paid
        if 'go/' in message.content.lower():
            matches = re.search(r'(?:^|[\n ])(?:[([<\"\'*`]+)?(https?://)?go/((#?[-\w_]+)(/([-\w_.~:/?#[\]@!$&\'()*+,;=%]+))?)', message.content)
            if matches:
                link = matches.group(2)
                await message.channel.send(f'https://golinks.io/{link}')
