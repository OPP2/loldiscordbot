import discord
from discord.ext import commands
import os

app = commands.Bot(command_prefix='.')
token = os.environ['BOT_TOKEN']


@app.event
async def on_ready():
    game = discord.Game("//")
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=game)


@app.command(aliases=['전적검색', 'ㅈㅈ'])
async def 전적(ctx, summoner_name):
    url = "https://www.op.gg/summoner/userName=" + summoner_name
    # print(url)
    # webbrowser.open(url)
    await ctx.send(url)


@app.command(aliases=['챔프', 'ㅊㅍ'])
async def 챔피언(ctx, champion_name):
    url1 = "https://www.op.gg/champion/%s/statistics" % champion_name
    # print(url1)
    # webbrowser.open(url1)
    await ctx.send(url1)


@app.command(aliases=['도움말'])
async def 도움(ctx):
    space = 'ㅤ'

    embed = discord.Embed(title=f"< > 칸안에 입력할때는 띄어쓰기X", description=f' ')

    embed.add_field(name=space, value=space, inline=False)

    embed.add_field(name=f'소환사 정보 검색', value=f'!전적 <소환사이름>', inline=False)

    embed.add_field(name=space, value=space, inline=False)

    embed.add_field(name=f'챔피언 정보 검색', value=f'!챔피언 <챔피언이름>', inline=False)
    await ctx.send(embed=embed)


app.run(token)
