import discord
from discord.ext import commands
import os

app = commands.Bot(command_prefix='.')
token = os.environ['BOT_TOKEN']


@app.event
async def on_ready():
    game = discord.Game(".도움")
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


@app.command(aliases=['도움말', 'ㄷㅇ'])
async def 도움(ctx):
    space = 'ㅤ'
    embed = discord.Embed(title=f"< > 칸안에 입력할때는 띄어쓰기X", description=f' ')
    embed.add_field(name=space, value=space, inline=False)
    embed.add_field(name=f'소환사 정보 검색', value=f'.전적 <소환사이름>', inline=False)
    embed.add_field(name=space, value=space, inline=False)
    embed.add_field(name=f'챔피언 정보 검색', value=f'.챔피언 <챔피언이름>', inline=False)
    await ctx.send(embed=embed)

@app.command()
async def embed(ctx):
    embed1 = discord.Embed(title="Example Embed", description="이것은 Embed입니다.", color=0x00ff56)
    embed.set_thumbnail(url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fnamu.wiki%2Fw%2F%25EB%25A6%25AC%25EA%25B7%25B8%2520%25EC%2598%25A4%25EB%25B8%258C%2520%25EB%25A0%2588%25EC%25A0%2584%25EB%2593%259C%2F%25EB%259E%25AD%25ED%2581%25AC%2520%25EA%25B2%258C%25EC%259E%2584&psig=AOvVaw3iF3jdC9kOz2TBlgSsONk0&ust=1632474777816000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCJjGqczglPMCFQAAAAAdAAAAABAD")

app.run(token)
