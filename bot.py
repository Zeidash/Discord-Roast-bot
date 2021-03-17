import discord
from discord.ext import commands
import random

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '-', intents = intents, help_command=None)

roasty = ('Jsi malá ubrečená píča, debile', 'Proč ztrácíš můj čas, plebe?', 'Nestojíš ani za roast.','Ty jsi tak těžký že ani pružinky z Lipra tě nezvednou (Generální partneři roastu jsou: Liper.)','Slabý kus')
forcePasty = ('Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. **Ironic.** He could save others from death, but not himself.' , 'The dark side of the Force is a pathway to many abilities some consider to be unnatural.', 'You wanna buy some deathsticks?')

@client.event
async def on_ready():
    print('Bot is ready baby oh yes!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Eternal suffering and chronic depressoin -help"))
#@client.event
#async def on_member_join(member):
#    print(f"Gods of the afterlife, spare my arse, to which curse do I owe {member}'s presence?.")

#@client.event
#async def on_member_remove(member):
#    print(f"{member} odešel, good riddance.")   

@client.command()
async def roast(ctx):
    i = random.randint(0, 4)
    roast = roasty[i]
    await ctx.send(roast)

@client.command()
async def force(ctx):
    i = random.randint(0, 2)
    pasta = forcePasty[i]
    await ctx.send(pasta)

@client.command()
async def vasek(ctx):
    await ctx.send('Ostříhej se :).')

@client.command()
async def help(ctx):
    await ctx.send('```list všech příkazů \n -roast | Dostaneš náhodný roast.    \n -vasek | Já fakt nevim proč jsem to přidal. \n -playlist | Pošle link na award winning playlist. \n -force | Pošle náhodnou Star Wars pastu. \n -pp | Zjisti jak obdařen jsi. \n -doinb | DoinB copypasta z 2019 \n https://twitter.com/selfmade_LoL/status/1288949960298450944?s=20```')

@client.command()
async def playlist(ctx):
    await ctx.send('https://youtu.be/9GUQUgmt1zg')

@client.command()
async def pp(ctx):
    komentar = '';
    i = random.randint(10, 250)
    i = i/10
    if i < 5:
        komentar = 'Tvoje pp dosahuje chabých rozměrů - '
    elif i < 10:
        komentar = 'Zklamání, něco jako Star Wars 8/9 - '
    elif i < 15:
        komentar = 'Mohlo by to být i horší - '
    elif i < 20:
        komentar = 'Gratuluji, ppgode - '
    elif i <= 25:
        komentar = 'Měl bys nosit jen dlouhé kalhoty - '
    komentar += str(i) + ' cm'
    await ctx.send(komentar)

@client.command()
async def doinb(ctx):
    await ctx.send('DOINB RYZE HACK？英雄联盟 400 CS 24 MIN DOINB RYZE HACK？英雄联盟 400 CS 24 MIN DOINB RYZE HACK？英雄联盟 400 CS 24 MIN DOINB RYZE HACK？英雄联盟 400 CS 24 MIN DOINB RYZE HACK？英雄联盟 400 CS 24 MIN')

client.run('ODIxNTIxMDIwMDM5OTg3MjMw.YFE7Eg.x06i_mWtMwMNJAnZ3FVJ2HcqCuU')
