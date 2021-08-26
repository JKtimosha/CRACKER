import discord
from discord.ext import commands
import asyncio
import requests
import random
import aiohttp
from datetime import datetime


class Main(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(aliases = ["курс-биткоина", "btc", "биток", "бк", "к-б"])
	async def биткоин(self, ctx):
		r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
		value = r['bpi']['USD']['rate']
		await ctx.send(embed = discord.Embed(title = "Курс биткоина",
			description = f"__Составляет:__ **{value}** долларов",
			timestamp = datetime.utcnow(),
			color = discord.Colour(0x9b59b6)))

	@commands.command()
	async def cum(self, ctx):
		channel_nsfw = ctx.channel.is_nsfw()
		if channel_nsfw:
			r = requests.get("https://nekos.life/api/v2/img/cum")
			res = r.json()
			em = discord.Embed(color = discord.Colour(0x71368a))
			em.set_image(url=res['url'])
			await ctx.send(embed=em)
		else:
			await ctx.send(embed = discord.Embed(title = "Ошибка",
				description = f"Но параметр канала {ctx.channel.mention} должен быть NSFW, чтоб использовать NSFW команды",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x71368a)))
	@commands.command(aliases = ["лезби"])
	async def lesbian(self, ctx):
		channel_nsfw = ctx.channel.is_nsfw()
		if channel_nsfw:
			r = requests.get("https://nekos.life/api/v2/img/les")
			res = r.json()
			em = discord.Embed(color = discord.Colour(0x71368a))
			em.set_image(url=res['url'])
			await ctx.send(embed=em)
		else:
			await ctx.send(embed = discord.Embed(title = "Ошибка",
				description = f"Но параметр канала {ctx.channel.mention} должен быть NSFW, чтоб использовать NSFW команды",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x71368a)))        		
	@commands.command(aliases = ["минет", "миньет"])
	async def blowjob(self, ctx):
		channel_nsfw = ctx.channel.is_nsfw()
		if channel_nsfw:
			r = requests.get("https://nekos.life/api/v2/img/blowjob")
			res = r.json()
			em = discord.Embed(color = discord.Colour(0x71368a))
			em.set_image(url=res['url'])
			await ctx.send(embed=em)
		else:
			await ctx.send(embed = discord.Embed(title = "Ошибка",
					description = f"Но параметр канала {ctx.channel.mention} должен быть NSFW, чтоб использовать NSFW команды",
					timestamp = datetime.utcnow(),
					color = discord.Colour(0x71368a)))
	@commands.command(aliases = ["секс"])
	async def sex(self,ctx, member: discord.Member):
		r = requests.get("https://nekos.life/api/v2/img/blowjob")
		res = r.json()
		embed = discord.Embed(description = f"{ctx.author.mention} занялся сексом с {member.mention}",
			color = discord.Colour(0x9b59b6))
		embed.set_image(url = res['url'])
		await ctx.send(embed = embed)
	@commands.command()
	async def anal(self, ctx):
		channel_nsfw = ctx.channel.is_nsfw()
		if channel_nsfw:
			r = requests.get("https://nekos.life/api/v2/img/anal")
			res = r.json()
			embed = discord.Embed(color = discord.Colour(0x9b59b6))
			embed.set_image(res['url'])
			await ctx.send(embed=embed)
		else:
			await ctx.send(embed = discord.Embed(title = "Ошибка",
					description = f"Но параметр канала {ctx.channel.mention} должен быть NSFW, чтоб использовать NSFW команды",
					timestamp = datetime.utcnow(),
					color = discord.Colour(0x71368a)))			
	@commands.command()
	async def tits(self, ctx):
		channel_nsfw = ctx.channel.is_nsfw()
		if channel_nsfw:
			r = requests.get("https://nekos.life/api/v2/img/tits")
			res = r.json()
			embed = discord.Embed(color = discord.Colour(0x9b59b6))
			embed.set_image(res['url'])
			await ctx.send(embed = embed)
		else:
			await ctx.send(embed = discord.Embed(title = "Ошибка",
					description = f"Но параметр канала {ctx.channel.mention} должен быть NSFW, чтоб использовать NSFW команды",
					timestamp = datetime.utcnow(),
					color = discord.Colour(0x71368a)))


	@commands.command()
	async def время(self, ctx):
		await ctx.send(embed = discord.Embed(title = None,
			description = f"{datetime.utcnow()}",
			timestamp = datetime.utcnow(),
			color = discord.Colour(0x9b59b6)))
	@commands.command()
	async def рандом(self, ctx, *, members):
		message = await ctx.send(embed = discord.Embed(title = "И выиграл у нас...",
			description = f"{random.choice(members)}, поздравляем!",
			timestamp = datetime.utcnow(),
			color = discord.Colour(0x9b59b6)))
	@commands.command()
	async def пинг(self, ctx):
		await ctx.send(embed = discord.Embed(title = 'Понг!',
			description = f":ping_pong: {self.bot.latency * 1000}ms!",
			timestamp = datetime.utcnow(),
			color = discord.Colour(0x9b59b6)))
	




def setup(bot):
	bot.add_cog(Main(bot))