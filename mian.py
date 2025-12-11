import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!s", intents=intents)

token = "" # // ใส่โทเค็นบอท
ROLE_ID = 1363063994679689226 # // ไอดียศนะจ๊ะ

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(
        name="Yoghurt GG", url="https://www.twitch.tv/IKGA"))
    print(f'บอทออนไลน์แล้ว: {bot.user}')

class RoleButton(discord.ui.View):
    def __init__(self, role: discord.Role):
        super().__init__(timeout=None)
        self.role = role
    
    @discord.ui.button(label="Click Me", style=discord.ButtonStyle.blurple, emoji="<a:checkmark:1241270268618608762>")
    async def give_role(self, interaction: discord.Interaction, button: discord.ui.Button):
        user = interaction.user
        if self.role in user.roles:
            await user.remove_roles(self.role)
            await interaction.response.send_message(f"คุณได้ลบยศ `{self.role.name}` ออกแล้ว!", ephemeral=True)
        else:
            await user.add_roles(self.role)
            await interaction.response.send_message(f"คุณได้รับยศ `{self.role.name}` แล้ว!", ephemeral=True)
            
@bot.command()
async def role(ctx):
    await ctx.message.delete()	
    guild = ctx.guild
    role = guild.get_role(ROLE_ID)
    if role is None:
        await ctx.send("ไม่พบยศนี้ในเซิร์ฟเวอร์")
        return

    embed = discord.Embed(
        title="กดปุ่มรับยศ", 
        description="```อย่าลืมกดรับยศก่อนจะเข้าดิสมาด้วยนะครับ```", 
        color=discord.Color.blue()
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/965908048608645131/1351897963210739712/banner.png")

    view = RoleButton(role)
    await ctx.send(embed=embed, view=view)

bot.run(token)