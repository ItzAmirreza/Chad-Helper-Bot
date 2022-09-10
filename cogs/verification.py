import discord
from discord.ext import commands
import asyncio


class Verification(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.executed = False

    @commands.Cog.listener()
    async def on_ready(self):
        client = self.client
        if self.executed:
            return
        self.executed = True
        client.add_view(self.VerifyView())

    class VerifyView(discord.ui.View):

        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label="Verify", style=discord.ButtonStyle.green, custom_id=f"verify", emoji="✅")
        async def green(self, interaction: discord.Interaction, button: discord.ui.Button,):
            member = interaction.user
            verified_role = interaction.client.get_guild(
                902975048514678854).get_role(1014801316410818630)
            await member.add_roles(verified_role)
            await interaction.response.send_message("Welcome!, you have been verified!", ephemeral=True)

    @commands.command(name="dummyverify")
    async def dummyverify(self, ctx):
        embed = discord.Embed.from_dict(
            {
                "description": "Greetings! 👋\n\nWe provide support for the plugin as well as your suggestions, bug reports and sneak peaks into upcoming updates, GitHub logs, pre-released jars download links and the list goes on.\nAlso, it is a place for you to interact with the developers of the plugin.\n\nBefore continuing, make sure you have read <#1014618505129238568> as well as <#940910748031410236> for questions that are asked previously.\n\nYou may also pick some useful roles up after the verification in the **🤏│pick-roles** channel.\n\nFinally to verify yourself, **please click on the \"✅ Verify\"  button below this message. **",
                "color": 16747146,
                "author": {
                    "name": "Welcome to the EZ Chest Shop plugin Discord server",
                    "icon_url": "https://cdn.discordapp.com/attachments/902981609240797264/1014785235365404672/New_ECS_emoji.png"
                },
                "footer": {
                    "text": "By verifying, you agree that you have read and accepted the rules provided in rules channel."
                },
                "image": {
                    "url": "https://cdn.discordapp.com/attachments/1014617561767346256/1014796869588746261/unknown.png"
                }
            }
        )
        view = self.VerifyView()
        await ctx.send(embed=embed, view=view)

    @commands.command()
    async def test(self, ctx):
        print("Salam piaze golam")


async def setup(client):
    await client.add_cog(Verification(client))
    print("Verification LOADED")
