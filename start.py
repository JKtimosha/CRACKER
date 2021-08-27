import discord
import os
import sys
from datetime import datetime
from discord.ext import commands
from Cybernator import Paginator
import colorama
colorama.init()
os.system("cls")
intents = discord.Intents.all()
intents.members = True
banner = f"""

{colorama.Fore.RED}
Logged as botuser 

"""

bot = commands.Bot(command_prefix = "f.", intents = intents)

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(activity=discord.Streaming(
        name=f"{len(bot.guilds)} guilds",url = "https://www.twitch.tv/monstercat")))




			
@bot.command()
async def exit(ctx):
	for role in ctx.guild.roles:
		print(role.color)

bot.remove_command("help")
@bot.group(invoke_without_command = True)
async def help(ctx, arg1 = None):
	if arg1 is None:
		embed111 = discord.Embed(title = "Помощь",
			description = f"Префикс: `{ctx.prefix}`\nКатегории помощи:\n__1.__  `Фан`\n__2.__ `Модерация`\n__3.__ `логи`\n__4.__ `Саппорт`\n__5.__ `NSFW`",
			timestamp = datetime.utcnow(),
			color = discord.Colour(0x9b59b6))
		embed = discord.Embed(title = "Модерация",
			description = f"`{ctx.prefix}ban` - забанить участника\n`{ctx.prefix}kick` - забанить участника\n`{ctx.prefix}leaveban` - человек который покинет гильдию автоматически получит бан\n`{ctx.prefix}clear` - очистить определёное количество сообщений",
			timestamp = datetime.utcnow(),
			color = discord.Colour(0x9b59b6))
		embed1 = discord.Embed(title = 
			"фан",
			description = f"`{ctx.prefix}биткоин` - показать курс биткоина\n`{ctx.prefix}время` - показать время\n`{ctx.prefix}рандом` - выбрать рандомное число\n`{ctx.prefix}пинг` - пинг бота",
			timestamp = datetime.utcnow(),
			color = discord.Colour(0x9b59b6)
		)
		embed2 = discord.Embed(title = "Саппорт",
			description = f"`{ctx.prefix}report` - пожаловаться на краш бота\n`{ctx.prefix}support` - поддержать проект\n`{ctx.prefix}idea` - кинуть идею для бота",
			color = discord.Colour(0x9b59b6))
		embed3 = discord.Embed(title = "NSFW", description = f"`{ctx.prefix}lesbian` - лезбипорно\n`{ctx.prefix}blowjob` - минет\n`{ctx.prefix}cum` - suck\n`{ctx.prefix}anal` - анал\n`{ctx.prefix}tits` - сиськи",
			color = discord.Colour(0x9b59b6))

		list = [embed111, embed, embed1, embed2, embed3]
		message = await ctx.send(embed=embed111)
		page = Paginator(bot, message, only=ctx.author, use_more=False, embeds=list)
		await page.start()


@bot.event
async def on_mention(ctx):
	await ctx.send(embed = discord.Embed(title = None, 
		description = f"Что? Мой префикс: {ctx.prefix}\nХелп команда - {ctx.prefix}",
		timestamp = datetime.utcnow(),
		color = discord.Colour(0x9b59b6)))
for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		bot.load_extension(f"cogs.{f[:-3]}")
@bot.event
async def on_command_error(ctx, error):
	channel = bot.get_channel(863773962835984384)
	await channel.send(embed = discord.Embed(description = f"{error}", color = discord.Colour.red()))
try:
	bot.run("ODczNTIzNTgzMjE1ODkwNDQy.YQ5qOw.rlahBw03lnbBXFmYYk6FUJWH91U")
except KeyboardInterrupt:
	sys.exit()