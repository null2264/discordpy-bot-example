import time


from discord.ext import commands


class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(example=["ping"])
    async def ping(self, ctx):
        """
        Show bot's ping.
        """
        websocket = round(self.bot.latency*1000, 2)

        ping_start = time.perf_counter()
        msg = await ctx.send(f"Pong! `{websocket}` ms")
        ping_end = time.perf_counter()
        typing = (ping_end - ping_start) * 1000
        return await msg.edit(content=f"Pong! `{websocket}` ms | `{round(typing, 2)}` ms")


def setup(bot):
    bot.add_cog(ExampleCog(bot))
