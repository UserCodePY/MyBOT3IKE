import discord
import asyncio
import random
import io
import datetime
import time
from discord.ext.commands import Bot
from discord.ext import commands

  
Client = discord.Client()
bot_prefix= "!"
client = commands.Bot(command_prefix=bot_prefix)
  
@client.event
async def on_ready():
    print("Bot Online! Go Discord Test it Out!")
    await client.change_presence(game=discord.Game(name='By 3IKE | Version 2.3.03'))

@client.event
async def on_member_join(member):
    server = member.server.default_channel
    fmt = ":tada: **Welcome to {1.name}**, {0.mention}, Please Read The Rules And Enjoy! :tada:"
    await client.send_message(discord.Object(id='418001869781205004'),(server, fmt.format(member, member.server)))

@client.event
async def on_member_remove(member):
    server = member.server.default_channel
    fmt = "{0.mention} Has Left The Server :wave:"
    await client.send_message(discord.Object(id='418001869781205004'),(server, fmt.format(member, member.server)))
    



@client.event
async def on_message (message):
    if message.author == client.user:
        return
    elif message.content.startswith("!ping"):
        embed=discord.Embed(description="**Pong Ping ? Ping Pong**  :joy: {0.author.mention}".format(message),color=0xff0000)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith ("!ask"):
        await client.send_message(message.channel, random.choice(["It is certain ",
                                                                  "It is decidedly so ",
                                                                  "Without a doubt ",
                                                                  "Yes, definitely ",
                                                                  "You may rely on it ",
                                                                  "As I see it, yes ",
                                                                  "Most likely ",
                                                                  "Outlook Looks Good ",
                                                                  "Yes Bro  ",
                                                                  "Signs point to yes ",
                                                                  "Reply hazy try again ",
                                                                  "Ask again later ",
                                                                  "Better not tell you now ",
                                                                  "Cannot predict now ",
                                                                  "Concentrate and ask again ",
                                                                  "Don't count on it ",
                                                                  "My reply is no ",
                                                                  "My sources say no ",
                                                                  "Outlook not so good ",
                                                                  "Very doubtful "]))

     
    elif message.content.startswith("!say"):
        variable = message.content[len('!say'):]
        if variable == "@everyone":
            await client.send_message(message.channel, "Nice Try ! You Think This is Funny :rage: **If You Do Again BAN**")
        elif variable == "@here":
            await client.send_message(message.channel, "Nice Try ! You Think This is Funny :rage: **If You Do Again BAN**")
        else:
            await client.send_message(message.channel, variable)

    elif message.content.startswith("!beep"):
        embed=discord.Embed(description="**Beep Boop** Boop Beep ? :joy: {0.author.mention}".format(message),color=0x00ff00)
        await client.send_message(message.channel, embed=embed)

    elif message.content.startswith("!invite"):
        emb = (discord.Embed(description=":link: Invite Link For This Server:-https://discord.gg/RzVTWnF {0.author.mention}".format(message), color=0xff0000))
        emb.set_author(name="Invite Link ", icon_url='https://images-ext-2.discordapp.net/external/PsZQiLXH8YrE7E5YVdMBxVlap2he9d3RU719X5Z_bbM/%3Fsize%3D128/https/cdn.discordapp.com/icons/418001869781205002/827549c65c67ade60b8f3cb80a134611.jpg?width=80&height=80')
        await client.send_message(message.channel, embed=emb)

    elif message.content.startswith("!help"):
        emb = (discord.Embed(description="You Can Get Help With Me Ask My Father <@429118689367949322> :man: :white_check_mark: ", color=0xff0000))
        emb.set_author(name="Help ", icon_url='https://images-ext-2.discordapp.net/external/PsZQiLXH8YrE7E5YVdMBxVlap2he9d3RU719X5Z_bbM/%3Fsize%3D128/https/cdn.discordapp.com/icons/418001869781205002/827549c65c67ade60b8f3cb80a134611.jpg?width=80&height=80')
        await client.send_message(message.channel, embed=emb)

    elif message.content.startswith("!cookie"):
        emb = (discord.Embed(description=" Here A Tasty Cookie Eat This and Get Fat ! :joy: | :cookie:   ", color=0xff8040))
        emb.set_author(name="Cookie Market  ", icon_url='https://cdn.discordapp.com/attachments/418001869781205004/429852670883266560/08c483393c3109ec7e69f7e3c47336a0.png')
        await client.send_message(message.channel, embed=emb)                               
                            
    elif message.content.startswith("!report"):
        variable = message.content[len('!report'):]
        if variable == "3IKE Spams":
            await client.send_message(message.channel, "Nice Try ! You Think This is Funny :rage: **If You Do Again BAN**")
        else:
            await client.send_message(discord.Object(id='418001869781205004'),(message.channel, variable))

    elif message.content.startswith("!rank"):
        embed=discord.Embed(title="Rank Legend", description="Your Rank Is Legend  {0.author.mention} :wink:".format(message), color=0xff0000)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/GHh2mEtjnr-WOTqfWwMRUOr3XTjcYXBnq1oPdf3woQ8/https/i.imgur.com/0hZ27iG.png?width=58&height=54")
        embed.set_footer(text="Version 32.3 By 3IKE | This Command is Made For Trolling Purposes ")
        await client.send_message(message.channel, embed=embed)
    
    elif message.content.startswith("!uptime"):
        await client.send_message(message.channel, "`Ich bin schon {0} stunde/n und {1} minuten online auf {2}. `".format(hour, minutes, message.server))
    

    elif message.content.startswith("!tank"):
        if message.author.id == "429118689367949322":
            embed=discord.Embed(title="Tank Online", url="http://tankionline.com" ,description="<@429118689367949322>" ,color=0xff0000)
            embed.set_author(name="Your Current Tank | NickName:- ARSKILLS", url="https://cdn.discordapp.com/attachments/418005628255207424/430309505314717717/logo.png",icon_url="https://cdn.discordapp.com/attachments/418005628255207424/430309505314717717/logo.png")
            embed.add_field(name="Turrent", value="Railgun M3", inline=True)
            embed.add_field(name="Hull" , value="Wasp M3", inline=True)
            embed.add_field(name="K/D", value="2.30", inline=True)
            embed.add_field(name="Gold Boxes", value="115", inline=True)
            embed.set_footer(text="Version • 3.62 • By 3IKE  | Ask How to Update Your Profile From My Father  ")
            await client.send_message(message.channel, embed=embed)
    
        else:
            embed=discord.Embed(title="Tank Online", url="http://tankionline.com", description="You Haven't Create a Profile Yet . Ask My Father <@429118689367949322> :no_entry:")
            embed.set_author(name="Error", url="https://cdn.discordapp.com/avatars/429243384729960470/92d1484dac2dcacf28439833edbfd497.jpg?size=2048",icon_url="https://cdn.discordapp.com/avatars/429243384729960470/92d1484dac2dcacf28439833edbfd497.jpg?size=2048")
            embed.set_footer(text="Version • 3.62 • By 3IKE | Create it Soon ")
            await client.send_message(message.channel, embed=embed)
    
        

client.run("process.env.BOT_TOKEN")


