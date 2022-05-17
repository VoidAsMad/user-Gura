from keep_alive import keep_alive
import discord
from discord.ext import commands
import discord_slash
from discord_slash import SlashCommand, SlashContext  
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
import datetime
from discord_slash.utils.manage_commands import create_option, create_choice
import asyncio
from discord.ext import tasks
from itertools import cycle
import random

from command.docs import *
from command.role import *
from command.user import *
from command.send import *
from command.warn import *
from command.language import *

import os
import sys
import urllib.request
import json

import urllib

from urllib.request import Request

import bs4

import koreanbots
from koreanbots.integrations.discord import DiscordpyKoreanbots



client_id = "mFt9JE_EBjb5dvMwlB5F"
client_secret = "ozWF8mnOBa"

cred = credentials.Certificate('user-gura-firebase-adminsdk-71eku-125d067d26.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://user-gura-default-rtdb.firebaseio.com/'
})

bot = commands.Bot(command_prefix=['?'], intents=discord.Intents.all())
slash = SlashCommand(bot,   sync_commands=True)
kb = DiscordpyKoreanbots(bot, 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijk2ODE0NzY2NTY0MjcyOTU3MyIsImlhdCI6MTY1MTQxMjE0Nn0.TyVOMkMLqyvyI-MjDw5CmiOP-Mn_DL6YE-puumzZp266uJP5cTPSrqzlFfoFehkHie0V7bWSsZVcfP4jtJXChrvcQ2yrtC-6SI0y12B9YAFZCbOswugAZsLmRmIiARguMkhopZNUEcBcmm8e1aoOx2csukK0YWWyJE7dnLgFwes', run_task=True)



async def tr(lv):
  if lv < 20:
    ts = '브론즈'
    return ts

  if lv >= 20 and lv < 40:
    ts = '골드'
    return ts

    
  if lv >= 40 and lv < 60:
    ts = '골드'
    return ts
  if lv >= 60 and lv < 80:
    ts = '플래티넘'
    return ts

  if lv >= 80 and lv < 100:
    ts = '다이아'
    return ts

  if lv >= 100:
    ts = '마스터'
    return ts

  
@slash.slash(name="lvup", description = '당신의 구라를 레벨업 시킵니다.(쿨타임 5초)')
@commands.cooldown(1, 5, commands.BucketType.user)
async def lvup(ctx):
  dir = db.reference(f'lv/{ctx.author.id}/guralv')
  lvs = dir.get()
  if lvs == None:
    lvs = 0

  up = random.randrange(1,11)

  suc = random.randrange(1,101)
  print(suc)

  if lvs <= 10:
    lv = lvs + up
    dir = db.reference(f'lv/{ctx.author.id}')
    dir.update({'guralv' : lv})
    trs = await tr(lv)
    await ctx.reply(f'레벨업이 성공하였습니다!\n> `{lvs}LV` → `{lv}LV`\n> 등급 : **{trs}**')
    return None



  if suc <= 5:
    lv = 1
    dir = db.reference(f'lv/{ctx.author.id}')
    dir.update({'guralv' : lv})
    trs = await tr(lv)
    await ctx.reply(f'누군가의 방해로 인해 레벨이 초기화가 되었습니다...\n> `{lvs}LV` → `1LV`\n> 등급 : **{trs}**')
    return None

    
  elif suc <= 20 and suc > 5:
    lv = lvs - up
    dir = db.reference(f'lv/{ctx.author.id}')
    dir.update({'guralv' : lv})
    trs = await tr(lv)
    await ctx.reply(f'레벨업이 실패하였습니다...\n> `{lvs}LV` → `{lv}LV`\n> 등급 : **{trs}**')
    return None

  else:
    lv = lvs + up
    dir = db.reference(f'lv/{ctx.author.id}')
    dir.update({'guralv' : lv})
    trs = await tr(lv)
    await ctx.reply(f'레벨업이 성공하였습니다!\n> `{lvs}LV` → `{lv}LV`\n> 등급 : **{trs}**')
    return None
  


@lvup.error
async def lvup_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send(f"쿨타임 {round(error.retry_after, 2)}초가 남았어요.", hidden = True)

@bot.event
async def on_ready():
  print('로딩완료')
  await bot.change_presence(activity=discord.Game("/docs"))



async def check_admin(ctx):
  if not ctx.author.guild_permissions.manage_messages:
    embed = discord.Embed(
      title='오류(Error)', 
      description="", 
      color=0x4374D9
    )
    embed.add_field(
      name="오류내용(Error content)", 
      value='```\nYou do not have permission\n```', 
      inline=False
    )
    await ctx.reply(embed=embed, hidden = True)
    return 'No'


  
#docs
@slash.slash(name="docs",description="Gura 공식 문서입니다. 태그가 비어있으면 태그 목록을 불러옵니다")
async def docs(ctx, tag : str = '기본'):
  
  await cdocs(ctx, tag)


#Role
@slash.slash(name="add_role",description="유저에게 역할을 부여합니다.")
async def addroles(ctx, role : discord.Role, user : discord.Member):
  c = await check_admin(ctx)
  if c == "No":
    return None
  await addrole(ctx, role, user)


@slash.slash(name="remove_role",description="유저에게 역할을 제거합니다.")
async def removeroles(ctx, role : discord.Role, user : discord.Member):
  c = await check_admin(ctx)
  if c == "No":
    return None
  await removerole(ctx, role, user)
  
#User
@slash.slash(name="kick",description="유저를 추방합니다.(재입장가능)")
async def kicks(ctx, user : discord.Member, reason = None):
  c = await check_admin(ctx)
  if c == "No":
    return None
  await kick(ctx, user, reason)
  
@slash.slash(name="ban",description="유저를 차단합니다.(재입장불가능)")
async def bans(ctx, user : discord.Member, reason = None):
  c = await check_admin(ctx)
  if c == "No":
    return None
  await ban(ctx, user, reason)

@slash.slash(name="send",description="메세지를 보냅니다.")
async def sends(ctx, channel : discord.TextChannel, message : str):
  c = await check_admin(ctx)
  if c == "No":
    return None
  await channel.send(message)
  await ctx.reply(f"<#{channel.id}>에게 메세지를 보냈습니다.")

@slash.slash(name="embed",description="임베드를 보냅니다.")
async def embeds(ctx, channel : discord.TextChannel, title : str, description : str, name : str = '없음', value : str = '없음'):
  c = await check_admin(ctx)
  if c == "No":
    return None
  await sendembed(ctx, title, description, name, value, channel)

@slash.slash(name="warn",description="경고를 부여합니다.")
async def warns(ctx, user : discord.Member):
  c = await check_admin(ctx)
  if c == "No":
    return None

  await warn(ctx, user)
  

@slash.slash(name="unwarn",description="경고를 삭제합니다.")
async def unwarns(ctx, user : discord.Member):
  c = await check_admin(ctx)
  if c == "No":
    return None

  await unwarn(ctx, user)

@slash.slash(name="warns",description="받은 경고횟수를 확인합니다.")
async def mywarns(ctx, user : discord.Member = None):
  c = await check_admin(ctx)
  if c == "No":
    return None

  await mywarn(ctx, user)

  

@slash.slash(name="language",description="언어를 변경합니다.")
async def languages(ctx, select : str = '목록'):  
  c = await check_admin(ctx)
  if c == "No":
    return None
  await language(ctx, select)


@slash.slash(name="gura",description="구라 일러스트를 출력합니다.")
async def image(ctx):
  search = ['gura', 'Gura', 'Gawr Gura', 'gawr gura']
  search = random.choice(search)
  encText = urllib.parse.quote(search)
  url = "https://openapi.naver.com/v1/search/image?query=" + encText

  request = urllib.request.Request(url)
  request.add_header("X-Naver-Client-Id",client_id)
  request.add_header("X-Naver-Client-Secret",client_secret)
  response = urllib.request.urlopen(request)
  rescode = response.getcode()

  # 이미지 저장 경로

  if(rescode==200):
    response_body = response.read()
    result = json.loads(response_body)
    img_list = result['items']


    a = len(img_list)
    s = int(random.randrange(1,a))
    img = img_list[s]
    await ctx.send(img['link'])




    '''
    response_body = response.read()
    result = json.loads(response_body)
    img_list = result['items']

    print(result['items'])

    for i, img_list in enumerate(img_list, 2):
        
        # 이미지링크 확인
        await ctx.send(img_list['link'])
        print(img_list)      
        break

    '''
        
  else:
    print("Error Code:" + rescode)


@slash.slash(name="clear",description="메세지를 삭제합니다.")
async def clear(ctx, amount : int):
  c = await check_admin(ctx)
  if c == "No":
    return None

  dir = db.reference(f'{ctx.guild.id}/lang')
  lang = dir.get()
  if lang == 'en':
    text = f"You can delete up to 200 messages."
    text2 = f'Deleted {amount} messages'

  else:
    text = f"메세지는 최대 100개 까지만 삭제할 수 있어요"
    text2 = f"{amount}개를 삭제 완료했어요!"
  if amount > 100:
    await ctx.reply(text, hidden = True)
    return None
  await ctx.channel.purge(limit=amount)
  msg = await ctx.send(text2)
  await asyncio.sleep(1.0)
  await msg.delete()


@slash.slash(name="avatar",description="프로필 사진을 출력합니다.")
async def avatar(ctx, user : discord.Member = None):
  if user == None:
    user = ctx.author
  embed = discord.Embed(
      title="", 
      description="", 
      color=0x4374D9
    )
  embed.set_image(url=f"{user.avatar_url}")
  embed.set_author(name=f"{user.name}#{user.discriminator}", icon_url=user.avatar_url)
  await ctx.send(embed = embed)  
  

@slash.slash(name="note",description="유저에 대해 메모를 합니다. 메모가 비어있으면 메모한 내용을 불러옵니다.")
async def note(ctx, user : discord.Member, memo : str = None):
  if memo == None:
    dir = db.reference(f'{ctx.guild.id}/{user.id}/note')
    note = dir.get()
    if note == None:
      await ctx.send(f'{user.mention}님에게 메모된 내용이 없습니다.', hidden = True)
      return None

    embed = discord.Embed(
      title=f'{user.name}님의 메모', 
      description=f"", 
      color=0x4374D9
    )
    embed.add_field(
      name="‎", 
      value=f"```md\n{note}\n```", 
      inline=False
    )
    await ctx.reply(embed=embed)

  else:
    dir = db.reference(f'{ctx.guild.id}/{user.id}/note')
    note = dir.get()
    dir = db.reference(f'{ctx.guild.id}/{user.id}')
    now = datetime.datetime.now()
    now = now + datetime.timedelta(hours=9)
    now = now.strftime("%Y-%m-%d %H시 %M분 %S초")
    if note == None:
      text = "\n" + now + "\n" + memo
    else:
      text = note + "\n" + now + "\n" + memo
    dir.update({'note' : text})
    await ctx.send('성공적으로 기록이 되었습니다!')

@slash.slash(name="note_reset",description="메모한 기록을 삭제합니다.")
async def notereset(ctx, user : discord.Member):
  dir = db.reference(f'{ctx.guild.id}/{user.id}/note')
  dir.delete()
  await ctx.send('성공적으로 기록이 삭제되었습니다!')

  
bot.run(token)
