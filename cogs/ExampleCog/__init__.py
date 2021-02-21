import cogs.ExampleCog._commands as exampleCmds


from discord.ext import commands


class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def ping(self, ctx):
    #     websocket = round(self.bot.latency*1000, 2)

    #     ping_start = time.perf_counter()
    #     msg = await ctx.send(f"Pong! `{websocket}` ms")
    #     ping_end = time.perf_counter()
    #     typing = (ping_end - ping_start) * 1000
    #     return await msg.edit(content=f"Pong! `{websocket}` ms | `{round(typing, 2)}` ms")


def setup(bot):
    cog = ExampleCog(bot)
    bot.add_cog(cog)

    # Get attribute from exampleCmds, hoping one of them is a command
    _ = [getattr(exampleCmds, attr) for attr in dir(exampleCmds)]
    for attr in _:
        # Try adding commands from attr listed in _
        try:
            command = attr()
            cog.__cog_commands__ += (command,) # Updates the __cog_commands__, this is to show up in HelpCommand
            command.cog = cog # Set the cog attribute with your instance, this is to make the library pass self
            bot.add_command(command) # Adds the command to the bot
        except TypeError:
            continue
