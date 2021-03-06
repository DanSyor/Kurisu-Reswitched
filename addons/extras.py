import datetime
import discord
import os
import random
import re
import string
from discord.ext import commands
from sys import argv

class Extras:
    """
    Extra things.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    prune_key = "nokey"

    @commands.command()
    async def robocop(self):
        """About the bot"""
        embed = discord.Embed(title="Robocop", color=discord.Color.green(), url="https://github.com/916253/Kurisu-Reswitched")
        embed.set_author(name="")
        embed.set_thumbnail(url="http://i.imgur.com/0iDmGQa.png")
        embed.description = "Based off of Kurisu by 916253 and ihaveamac"
        await self.bot.say("", embed=embed)

    @commands.command()
    async def membercount(self):
        """Prints the member count of the server."""
        await self.bot.say("{} has {:,} members!".format(self.bot.server.name, self.bot.server.member_count))

    @commands.has_permissions(ban_members=True)
    @commands.command(hidden=True)
    async def embedtext(self, *, text):
        """Embed content."""
        await self.bot.say(embed=discord.Embed(description=text))

    @commands.command(hidden=True)
    async def timedelta(self, length):
        # thanks Luc#5653
        units = {
            "d": 86400,
            "h": 3600,
            "m": 60,
            "s": 1
        }
        seconds = 0
        match = re.findall("([0-9]+[smhd])", length)  # Thanks to 3dshax server's former bot
        if match is None:
            return None
        for item in match:
            seconds += int(item[:-1]) * units[item[-1]]
        curr = datetime.datetime.now()
        diff = datetime.timedelta(seconds=seconds)
        # http://stackoverflow.com/questions/2119472/convert-a-timedelta-to-days-hours-and-minutes
        # days, hours, minutes = td.days, td.seconds//3600, (td.seconds//60)%60
        msg = "```\ncurr: {}\nnew:  {}\ndiff: {}\n```".format(
            curr,
            curr + diff,
            diff
        )
        await self.bot.say(msg)

    @commands.command(pass_context=True)
    async def rules(self, ctx, mention_user : discord.Member=None):
        """Post a link to the Rules"""
        if mention_user:
            await self.bot.say("{} Please review this servers rules here: <https://reswitched.team/discord/>".format(mention_user.mention))
        else:
            await self.bot.say("{} A link to the rules can be found here: <https://reswitched.team/discord/>".format(ctx.message.author.mention))

    @commands.command(pass_context=True)
    async def guides(self, ctx, mention_user : discord.Member=None):
        # links guides aimed at end-users
        guides_links = ["<https://guide.sdsetup.com/> by noahc3",
                        "<http://switchguide.xyz/> by noirscape",
                        "<https://switch.hacks.guide/> by Plailect"]
        if mention_user:
            await self.bot.say("{}\n{}".format(mention_user.mention, '\n'.join(guides_links)))
        else:
            await self.bot.say('\n'.join(guides_links))

def setup(bot):
    bot.add_cog(Extras(bot))
