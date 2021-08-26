import discord
import json
import requests



from pymongo import MongoClient
from discord import *
from discord import Forbidden
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import *
from aiohttp import ClientSession
from Cybernator import Paginator as pag



class ac(Cog):
	def __init__(self,bot):
		self.cluster = MongoClient("mongodb+srv://SqOzY:149005060abs@cluster0.prjyw.mongodb.net/anticrush?retryWrites=true&w=majority")
		self.db = self.cluster["anticrush"]
		self.xuy = self.cluster["whitelist"]

		self.databasa = self.xuy["whitelist"]

		self.channelcol = self.db["channels"]
		self.rolecol = self.db["roles"]
		self.categories = self.db["categories"]
		self.emoji = self.db["emoji"]
		self.stickers = self.db["stickers"]


		self.bot = bot
		self.stop = []



		self.bots = [310848622642069504,
		235088799074484224,
		740585412560420914,
		]
		self.raiders = [802620547925540944,
		675276010907893785,
		840580482264727582]
	@commands.command(aliases = ["добавить-восстановление", "сохранить","сохранить-сервер",
		"добавить-сохранение",
		"бекап",
		"backup",
		"add-backup"])
	@commands.has_permissions(administrator = True) 
	async def save(self, ctx):
		for gee in bot.guilds:
			if f'{ctx.guild.id}' in gee.name:
				await bot.remove_guild(ctx.guild.id)
		await bot.create_guild(f'{ctx.guild.id}')
		for gee in bot.guilds:
			if f'{ctx.guild.id}' in gee.name:
				for c in gee.channels:
					await c.delete()
				for cate in ctx.guild.categories:
					x = await gee.create_category(f"{cate.name}")
					for cn in cate.channels:
						if isinstance(cn, discord.VoiceChannel):
							await x.create_voice_channel(f"{cn}")
						if isinstance(cn, discord.TextChannel):
							await x.create_text_channel(f"{cn}")
					for i in gee.roles:
						await gee.create_role(name = i, color = discord.Colour.from_rgb(str(i.color)))
						try:
							await gee.edit(icon=ctx.guild.avatar_url)
						except:
							pass
		await ctx.send(embed = discord.Embed(title = 'успешно'))

	@commands.command(aliases = ["востановить"])
	async def load(self, ctx):
		for gee in bot.guilds:
			if f'{ctx.guild.id}' in gee.name:
				for cate in gee.guild.categories:
					x = await ctx.guild.create_category(f"{cate.name}")
				for cn in cate.channels:
					if isinstance(cn, discord.VoiceChannel):
						await x.create_voice_channel(cn)
					else:
						await x.create_text_channel(cn)
				for i in gee.roles:
					await ctx.guild.create_role(name = i, color = i.color)

				await ctx.send(embed = discord.Embed(description = "Succes",
					color = discord.Colour.orange()))
			else:
				await ctx.send(embed = discord.Embed(title ="Ошибка",
					description = "Вы не добавили востановление. Чтоб добавить его следуйте за таким примером: f.save",
					color = discord.Colour.red()))



	@commands.command(aliases = ["вайтлист"])
	@commands.has_permissions(administrator = True)
	async def whitelist(self ,ctx,*, member : int = None):
		if member is None:
			await ctx.send(embed = discord.Embed(title = "Отчет",
				description = "__Вы не задали следующий аргумент правильно, или не задали вобще! Следуйте за таким примером:__\n>f.вайтлист <айди пользователя & упоминание пользователя>",
				timestamp = datetime.utcnow(),
				color = discord.Colour.dark_blue()))
		else:
			if member is int:
				if self.databasa({"_id":ctx.guild.id}) == 0:
					self.databasa({"_id":ctx.guild.id,
						"members":[]})
					self.databasa.update_one({"_id":ctx.guild.id}, {"&set":{
						"members":[].append(member)
						}})
			


	@Cog.listener()
	async def on_ready(self):
		print("Anticrush is loaded")

	@commands.command(pass_context= True, aliases = ["стоп","завершить","end"])
	async def stop(self, ctx):
		if ctx.guild.id in self.stop:
			await ctx.send(embed = discord.Embed(title = "Отчет",
				description = "__Бот уже в стопе!__",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))
		else:
			self.stop.append(ctx.guild.id)
			await ctx.send(embed = discord.Embed(title = "Успешно!",
				description = "__Бот прекратил работу на вашем сервере__\n> __Чтоб начать достаточно написать `f.старт`__",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))

	@commands.command(aliases = ["getup", "старт", "начать"])
	async def start(self, ctx):
		if ctx.guild.id in self.stop:
			self.stop.remove(ctx.guild.id)
			await ctx.send(embed = discord.Embed(title = "Успешно",
				description = "__Бот продолжает свою работу на вашем сервере__",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))
		else:
			await ctx.send(embed = discord.Embed(title = "Обратный отчет",
				description = "__Бот все это время работал, возможно есть недочеты. Как их исправить?\n> 1. Поставьте роль бота выше всех\n> 2. Дайте ему право 'Администратор'. Готово",
				timestamp = datetime.utcnow(),
				color = discord.Colour.dark_red()))
	@Cog.listener()
	async def on_guild_channel_delete(self,channel):
		entry = await channel.guild.audit_logs(action = discord.AuditLogAction.channel_delete, limit = 1).get()
		if entry.user.id == channel.guild.owner_id:
			print("[-] ета овнер")
		elif entry.user.id in self.bots:
			pass
		elif channel.guild.id in self.stop:
			print("СТОП")

		else:
			if channel is discord.CategoryChannel:
				try:
					await entry.user.ban(reason = "Попытка крашнуть сервер")

					anal = await channel.guild.create_category(name = channel.name)
					await anal.edit(position = channel.position)
				except Exception:
					pass
			else:
				try:
					await entry.user.ban(reason = "Попытка крашнуть сервер!")

					anel = await channel.guild.create_text_channel(name = channel.name)
					await anel.edit(position = channel.position)
				except Exception:
					pass
	
	@Cog.listener()
	async def on_guild_channel_create(self, channel):
		entry = await channel.guild.audit_logs(action  = discord.AuditLogAction.channel_create, limit = 1).get()
		if entry.user.id == channel.guild.owner_id:
			print('[-] ета овнер')
		elif entry.user.id in self.bots:
			pass
		elif channel.guild.id in self.stop:
			print("ОН В СТОПЕЕЕ")
		else:
			try:
				await entry.user.ban(reason = "Попытка крашнуть сервер")

				await channel.delete()
			except Exception:
				pass


	
	@Cog.listener()
	async def on_guild_role_delete(self, role):
		entry = await role.guild.audit_logs(action = discord.AuditLogAction.role_delete, limit = 1).get()
		if entry.user.id == role.guild.owner_id:
			print("[-] ета овнер")
		elif entry.user.id in self.bots:
			pass
		elif role.guild.id in self.stop:
			print(f"[-] гильдия, которая имеет айди {role.guild.id} в стопе) ЕРРОР МАДАФАКА")
		else:
			try:
				await entry.user.ban(reason = "Попытка крашнуть сервер")


				await ctx.guild.create_role(name = role.name)
				role = discord.utils.get(role.guild.roles, name = role.name)
				await role.edit(position = role.position)
				await role.edit(Colour = role.colour)
			except Exception:
				pass

	


	@Cog.listener()
	async def on_message_delete(self, message):
		if not message.author.bot:
			#try:
			if message.content is message.mention:
				pass
			else:
				hook = await message.channel.create_webhook(name = message.author)
				async with ClientSession() as session:
					webhook = discord.Webhook.from_url(hook.url, adapter=discord.AsyncWebhookAdapter(session))
					await webhook.send(content=message.content, username=message.author.name, avatar_url=message.author.avatar_url)
			#except:
				#print("[-] Новый баг какойто в ивенте on_message_delete ЛЕТС ГО ФИКСИТЬ!")
	@Cog.listener()
	async def on_member_kick(self, member):
		entry = await member.guild.audit_logs(action = discord.AuditLogAction.kick,limit = 1).get()
		if entry.user.id == member.guild.owner_id:
			print("[-] ета овнер")
		elif entry.user.id in self.bots:
			pass
		elif member.guild.id in self.stop:
			print(f"[-] гильдия которая имеет айди {ctx.guild.id} в стопе это отчет если че")
		else:
			try:
				await entry.user.ban(reason = "Попытка крашнуть сервер")

			
				print("LOL")
			except Exception:
				pass

	@Cog.listener()
	async def on_member_ban(self, member):
		entry = await member.guild.audit_logs(action = discord.AuditLogAction.ban, limit = 1).get()
		if entry.user.id == member.guild.owner_id:
			pass
		elif entry.user.id in self.bots:
			pass
		elif member.guild.id in self.stop:
			print("FUCK мне лень писать")
		else:
			try:
				await entry.user.ban(reason = "Попытка крашнуть сервер")

				await member.ban()
			except Exception:
				pass

	@Cog.listener()
	async def on_member_join(self, member):
		if member.id in self.bots:
			try:
				await member.ban(reason = "Крашер & спамер - блеклист бота")
			except Exception:
				pass






def setup(bot):
	bot.add_cog(ac(bot))