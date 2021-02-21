import time


from discord.ext import commands


class Ping(commands.Command):
    def __init__(self):

        params = {
            "name": "ping",
        }

        async def function(self, ctx):
            websocket = round(self.bot.latency*1000, 2)

            ping_start = time.perf_counter()
            msg = await ctx.send(f"Pong! `{websocket}` ms")
            ping_end = time.perf_counter()
            typing = (ping_end - ping_start) * 1000
            return await msg.edit(content=f"Pong! `{websocket}` ms | `{round(typing, 2)}` ms")

        super().__init__(function, **params)

