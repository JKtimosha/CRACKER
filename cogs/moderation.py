import discord
import asyncio
import json



from datetime import datetime
from discord.ext import commands

prefix = "f."
class Main(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		self.cooldown = []

		self.cluster = MongoClient("mongodb+srv://SqOzY:149005060abs@cluster0.prjyw.mongodb.net/anticrush?retryWrites=true&w=majority")
		self.db = self.cluster["warns"]
		self.database = self.db["warns"]



	@commands.Cog.listener()
	async def on_ready(self):
		print(f"Moderation is ready! ")


	@commands.command(aliases = ["бан","забанить", "hammer","blacklist"])
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member:discord.User,*, reason = None):
		if member == None or member == ctx.author or member == ctx.guild.owner: 
			await ctx.send(embed = discord.Embed(title = "Неправильный заданный параметр",
				description = "__Неправильный заданный параметр__\nПочему он не правильный? - \n__1. Вы не можете забанить самого себя\n2. Вы могли вообще не указать пользователя, которого хотите забанить!__\n3. Вы не МОжете забанить владельца сервера",
				timestamp = datetime.utcnow(),
				color  = discord.Colour.dark_green()))
		elif type(member) == discord.Member:
			await ctx.guild.kick(member, reason=reason, delete_message_days=0)
			await ctx.send(embed = discord.Embed(title = member.display_name,
				description = "Был успешно забанен по причине: {}".format(reason),
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))
		else:
			mem = discord.Object(member)
			await ctx.guild.ban(
                mem, reason=reason, delete_message_days=0
            )
			await ctx.send(embed = discord.Embed(title = mem,
				description = "Был успешно забанен по причине: {}".format(reason),
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))


	@commands.command(aliases = ["кикнуть", "пнуть", "кик", "выпнуть"])
	@commands.has_permissions(kick_members = True)
	async def kick(self, ctx, member:discord.User = None,*, reason = None):
		if ctx.author.id == member.id or member.id == ctx.guild.owner_id:
			pass
		elif type(member) == discord.Member:
			await ctx.guild.kick(member, reason=reason, delete_message_days=0)
			await ctx.send(embed = discord.Embed(title = member.display_name,
				description = "Был успешно кикнут по причине: {}".format(reason),
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))
		else:
			mem = discord.Object(member)
			await ctx.guild.ban(
                mem, reason=reason, delete_message_days=0
            )
			await ctx.send(embed = discord.Embed(title = mem,
				description = "Был успешно кикнут по причине: {}".format(reason),
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))
	@commands.command()
	async def leaveban(ctx, *, reason = None):
		await ctx.send(embed = discord.Embed(title ="Мод включен",description = "Теперь человек, который покинет сервер будет автоматически забанен",
			timestamp = datetime.utcnow(),
			color = discord.Colour(0x9b59b6)))
		@commands.Cog.listener()
		async def on_member_leave(member):
			await member.ban(reason=reason)
	@commands.Cog.listener()
	async def on_guild_join(ctx):
		for channel in ctx.guild.text_channels:
			if channel.position == 1:
				await ctx.send(embed = discord.Embed(title = "Хелп",
					description = f"Спасибо, что добавили меня на свой сервер!\nМои небольшие параметры:\nПрефикс: {ctx.prefix}\nХелп команда: {ctx.prefix}help\nНаписан на: Python",
					timestamp = datetime.utcnow(),
					color = discord.Colour(0x9b59b6)))

	@commands.command(aliases = ["очистить", "clearchat","очистить_чат"])
	async def clear(self, ctx, limit:int = None):
		if limit is None:
			await ctx.send(embed = discord.Embed(title = "Ошибка..",
				description = "Неверный синтаксис команды! Действуйте за этим припмером:\n> `f.очистить <число от 1 до 10000>`",
				timestamp = datetime.utcnow(),
				color = discord.Colour.dark_red()))
		elif limit > 10000:
			await ctx.channel.purge(limit = 10000)
			await ctx.send(embed = discord.Embed(title = 'Успешно',
				description = f"Очищено 10000 сообщений",
				timestamp = datetime.utcnow(),
				color = discord.Colour.blue()
				))
		else:
			await ctx.channel.purge(limit=limit)
			await ctx.send(embed = discord.Embed(title = "Успешно!",
				description = f'Очищено {limit} сообщений!',
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))



def setup(bot):
	bot.add_cog(Main(bot))
