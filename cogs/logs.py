import discord
from discord import Forbidden
from datetime import datetime
from discord.ext import commands

prefix = ">"

class loggs(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.cha = None


	@commands.command()
	async def setlog_channel(self,ctx, channel:discord.TextChannel = None):
		if channel is None:
			await ctx.send(embed = discord.Embed(title = "Чтото пошло не так..",
				description = f"__Неверное использование команды, попробуйте как-то так:__\n> {prefix}setlog_channel **<айди канала или сам текстовый канал>**",
				timestamp = datetime.utcnow(),
				color = discord.Colour.red()))
		elif channel is int:
			self.log_channel_id = bot.get_channel(channel)
			await ctx.send(embed = discord.Embed(
				title = "Успешно!",
				description = f"Теперь логи сервера будут сохраняться в {channel.mention}",
				timestamp = datetime.utcnow(),
				color = discord.Colour.green()))
		else:
			self.channel = channel
			self.cha = channel
			await ctx.send(embed = discord.Embed(
				title = "Успешно!",
				description = f"Теперь логи сервера будут сохраняться в {channel}",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))
	@commands.Cog.listener()
	async def on_ready(self):
		print('Logs are ready')
	@commands.Cog.listener()
	async def on_member_ban(self, ctx, member):
		if self.channel is None:
			print("[-] channel is None")
		else:
			entry = await ctx.audit_logs(action = discord.AuditLogAction.ban, limit = 1).get()

			await self.channel.send(embed = discord.Embed(
				description = f"{entry.user.mention} __забанил участника__ **{member}** & \n> {member.mention}",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))

	@commands.Cog.listener()
	async def on_member_kick(self, ctx):
		if self.channel is None:
			print("[-] channel is None")
		else:
			entry = await ctx.audit_logs(action = discord.AuditLogAction.kick, limit = 1).get()
			await self.channel.send(embed = discord.Embed(
				description = f"{entry.user.mention} __кикнул участника__ **{member}** & \n> {member.mention}",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))

	@commands.Cog.listener()
	async def on_invite_create(self, invite):
		if self.cha is None:
			pass
		else:
			entry = await invite.guild.audit_logs(action = discord.AuditLogAction.invite_create, limit = 1).get()
			await self.channel.send(embed = discord.Embed(
				description = f"{entry.user.mention} __создал инвайт__ discord.gg/||{invite.code}|| & ||**{invite.code}**||",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))

	@commands.Cog.listener()
	async def on_guild_channel_create(self, channel):
		if self.cha is None:
			pass
		else:
			entry = await channel.guild.audit_logs(action = discord.AuditLogAction.channel_create, limit = 1).get()
			await self.cha.send(embed = discord.Embed(
				description = f"{entry.user.mention} __создал новый канал__ \n> {channel.mention}",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))

	@commands.Cog.listener()
	async def on_guild_channel_delete(self, channel):
		if self.cha is None:
			pass
		else:
			entry = await channel.guild.audit_logs(action = discord.AuditLogAction.channel_delete, limit = 1).get()

			await self.cha.send(embed = discord.Embed(
				description = f"{entry.user.mention} __удалил канал \n> **{channel}**__",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))

	@commands.Cog.listener()
	async def on_guild_role_create(self, role):
		if self.cha is not None:

			entry = await role.guild.audit_logs(action = discord.AuditLogAction.role_create, limit = 1).get()

			await self.channel.send(embed = discord.Embed(
				description = f"{entry.user.mention} __создал новую роль__ ->\n> {role.mention} ",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)))

	@commands.Cog.listener()
	async def on_guild_role_delete(self, role):
		if self.cha is not None:
			entry  = await role.guild.audit_logs(acion = discord.AuditLogAction.role_delete, limit = 1).get()

			await self.channel.send(embed = discord.Embed(
				description = f"{entry.user.mention} __удалил роль__ ->\n> **{role}**",
				timestamp = datetime.utcnow(),
				color =discord.Colour(0x9b59b6)))

	@commands.Cog.listener()
	async def on_invite_delete(self, invite):
		if self.cha is not None:
			entry = await invite.guild.audit_logs(action = discord.AuditLogAction.invite_delete, limit = 1).get()

			await self.cha.send(embed = discord.Embed(
				description = f"{entry.user.mention} __удалил инвайт__ ||**{invite.code}**||",
				timestamp = datetime.utcnow(),
				color = discord.Colour(0x9b59b6)
				))

	
	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		if before.display_name != after.display_name and self.cha is not None:
			await self.channel.sned(embed = discord.Embed(
			title = f"{before.display_name} изменил свое имя",
			description = f"{member.mention}\n**Предыдущее имя:** {before.display_name} **Нынешнее:** {after.display_name}",
			timestamp = datetime.utcnow(),
			color = discord.Colour(0xe91e63)))
	@commands.Cog.listener()
	async def on_message_edit(self, before, after, member):
		if before.message != after.message and self.cha is not None:
			embed = discord.Embed( 
				description = f"{member.mention} изменил своё сообщение",
				timestamp= datetime.utcnow(), 
				color = discord.Colour(0xe91e63))
			embed.add_field(name = "Сообщение **ДО** изменения",value= f"> {before.message}",inline = False)
			embed.add_field(name = "Сообщение **ПОСЛЕ** изменения",value = f"> {after.message}", inline = False)
			await self.channel.send(embed=embed)

	@commands.Cog.listener()
	async def on_guild_role_update(self, before, after):
		if before.name != after.name and self.cha is not None:
			await self.channel.send(embed = discord.Embed(title = "Изменили название роли",
								description=  f"> **Название ДО изменения:** {before.name}\n> **Название ПОСЛЕ изменения:** {after.name}",
								timestamp=  datetime.utcnow(),
								color = discord.Colour(0xe91e63)))
	@commands.Cog.listener()
	async def on_guild_channel_update(self, before, after):
		if before.name != after.name and self.cha is not None:
			embed = discord.Embed(title = f"Название канала {before.name} изменено",
								description= f"> **Предыдущее название:** {before.name}\n> **Нынешнее:** {after.name}", 
								timestamp = datetime.utcnow(),
								color = discord.Colour(0xe91e63))
			await self.channel.send(embed=embed)


def setup(bot):
	bot.add_cog(loggs(bot))
