#Automatically generated by Bot Generator
import discord
from discord import client
from discord.ext import commands
client = commands.Bot(command_prefix='-')
#You can change the prefix to whatever thing you want
@client.event 
async def on_ready(): 
 	 print('Bot starts working!') 
#You can delete that (It won't break your bot). It shows if bot is active or not 
client.run() #Your api goes here!
