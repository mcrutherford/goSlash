"""
File: goSlash.py
Author: Mark Rutherford
Created: 02/21/2023 2:30 PM
"""
import re
import threading

import discord
from discord.ext import commands


class SlashGo(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.lock = threading.Lock()

    @commands.command(name='go', help='Responds with a pong!')
    async def pingpong(self, ctx):
        await ctx.send('pong!')
