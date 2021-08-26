import discord
import json
import asyncio
from datetime import datetime
from discord.ext import commands

class support(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		self.cooldown = []
	@commands.command(aliases = ["пожаловаться",
		"жб", 
		"жалоба"])
	async def report(self, ctx, idof:int = None, *,reason:str=None):
		if idof is None:
			await ctx.send(embed = discord.Embed(title  = "Жалоба | Помощь",
				description= "> f.жалоба - показать данное сообщение\n> f.жалоба <айди краш бота> - пожаловаться на краш бота\n f.жалоба <айди краш бота> <Хотите указать другую инную причину? Пишите в этот аргумент>",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x71368a)))
		elif ctx.author.id in self.cooldown:
			await ctx.send(embed =discord.Embed(title = "Ошибка",
				description = f"__Вы не можете отправлять отправлять так много жалоб!__\n> Попробуйте чуть позже",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x71368a)))
		else:
			channel = await bot.get_channel(858772462250885151)
			await channel.send(embed = discord.Embed(title = 'Жалоба на краш бота!',
				description = f"> Айди бота: {idof}\n> Причина:{reason}\n> Инвайт: https://discord.com/oauth2/authorize?client_id={idof}&permissions=8&scope=bot\n> Подал жалобу: {ctx.author}\n> Подал жалобу(айди): {ctx.author.id}",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x71368a)))
			await ctx.send(embed = discord.Embed(title = 'Успешно',
				description = f"Жалоба была успешно отправлена и в течении 24 часов вам ответят!",
				timestamp = datetime.utcnow(),
				color=  discord.Colour(0x71368a)))
			self.cooldown.append(ctx.author.id)
			await asyncio.sleep(600)
			self.cooldown.remove(ctx.author.id)

	@commands.command(aliases = ["поддержать", "поддержать_проект"])
	async def support(self, ctx):
		await ctx.send(embed = discord.Embed(title = 'Support',
			description = "Хотите поддержать проект? Можете задонатить не большую суму, нам будет приятно) - ",
			timestamp = datetime.utcnow(),
			color = discord.Colour(0x71368a)))


	@commands.command(aliases = ["идея"])
	async def idea(self, ctx,*, idea = None):
		if idea is None:
			await ctx.send(embed = discord.Embed(description = "__Есть идеи? Мoжете предложить используя синтаксис типо такого:__\n> `f.идея <сама идея>`",
				timestamp = datetime.utcnow(),
				color = discord.Colour.green()))
		elif ctx.author.id in self.cooldown:
			await ctx.send(embed =discord.Embed(description = "__Ошибка.. но вы не можете отправлять так много идей, меньше чем 10минут!__\n> Повторите чуть позже",
				timestamp =datetime.utcnow(),
				color = discord.Colour.dark_red()))
		else:
			channel = await bot.get_channel(858775839000494120)
			await channel.send(embed = discord.Embed(title = "Новая идея",
				description = f">>> Новая идея от пользователя: {ctx.author} & {ctx.author.id}\nСама идея: {idea}",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x71368a)))
			await ctx.send(embed =discord.Embed(description = "Идея была отправлена! Спасибо, что помогаете проекту =)",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x71368a)))
			self.cooldown.append(ctx.author.id)
			await asyncio.sleep(600)
			self.cooldown.remove(ctx.author.id)
	





def setup(bot):
	bot.add_cog(support(bot))
