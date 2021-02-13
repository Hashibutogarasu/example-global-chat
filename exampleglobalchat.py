import time
import discord
print("Imported discord\n")

time.sleep(1)

TOKEN = 'Your Token Code'
print("Your token code was recognized.\n")

time.sleep(1)

client = discord.Client()
print("Discord was connected")

time.sleep(1)

@client.event
async def on_ready():
    print('Logged on')
    await client.change_presence(activity=discord.Game(name="EXAMPLE", type=1))

#botの処理本体開始

@client.event
async def on_message(message):
    if message.author.bot:
        
        return
    GLOBAL_CH_NAME = "crowglobal"
    if message.channel.name == GLOBAL_CH_NAME:

        await message.delete()

        channels = client.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]

        embed = discord.Embed(title="crowglobal",
            description=message.content, color=0x00bfff)

        embed.set_author(name=message.author.display_name, 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name}",
            icon_url=message.guild.icon_url_as(format="png"))

        for channel in global_channels:
            await channel.send(embed=embed)

#botの処理本体終了

client.run(TOKEN)

#参照:https://qiita.com/coolwind0202/items/061a08b0608d94fcb552
#参照:https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f
#参照:https://discordpy.readthedocs.io/ja/latest/faq.html#how-do-i-set-the-playing-status
