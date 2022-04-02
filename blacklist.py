import discord
import json
from discord.ext import commands

#BOT EVENT
@bot.event
async def on_message(message):
    
    if message.author.id == bot.user.id:
        return
    
    if message.author.id in bot.blacklisted_users:
        return
    
    if message.content.lower().startswith("help"):
        await message.channel.send("Run the help command with `.help`")
        
    await bot.process_commands(message)
    
        
#YOUR COMMAND
@bot.command()
@commands.is_owner()
async def blacklist(ctx, member: discord.User):
    channel = ctx.bot.get_channel(955134736395821066)
    
    embed = discord.Embed(title = "User Blacklisted", description = "A user was added to the blacklist list.", timestamp = ctx.message.created_at)
    embed.add_field(name = "Member Blacklisted:", value = f"{member.name} | {member.id}")
    
    bot.blacklisted_users.append(member.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].append(member.id)
    write_json(data, "blacklist")
    await ctx.send(f"**{member.name} | {member.id}** has been **BLACKLISTED** from all DiaMod services.")
    await channel.send(embed = embed)
    
    
    
    
#JSON STUFF

 def read_json(filename):
    with open(f"{cwd}/database/{filename}.json", "r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"{cwd}/database/{filename}.json", "w") as file:
        json.dump(data, file, indent = 4)
