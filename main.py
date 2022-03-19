import discord
import keep_alive
from discord.ext import commands
import json
with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
import random

bot = commands.Bot(command_prefix='i')


#中間
@bot.event
async def on_ready():
    print(">>Bot is online<<")


'''
@bot.event()
async def on_message(msg):
	if msg.content == '早安小冰冰' :
		await msg.channel.send('早ㄤ')
  await bot.process_commands(msg)
'''


#指令
@bot.command()
async def awa(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('awa怪物')


@bot.command()
async def all(ctx):
    await ctx.send(
        '``` awa    awa怪物 \n cat    叭噗 \n cute   ??????????? \n delete 刪訊息(idelete number) \n gg     \|/  \n ice    冰淇淋好好ㄘ \n liver  肝有兩顆! \n mao    好爽好爽,給我素(隨機) \n pink   破腦噁男 \n re     重複(ire message) \n sad    嗷嗷 \n sorry  對ㄅ起 \n velon  魔法! \n hug    隨機抱抱 \n sexdog  不可以色色狗狗(隨機)\n itod	truth or dare(itod 人數)```'
    )


@bot.command()
async def ice(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('冰淇淋好好ㄘ')


@bot.command()
async def mao(ctx):
    random_mao = random.choice(jdata['mao'])
    await ctx.channel.purge(limit=1)
    await ctx.send(content=random_mao)


@bot.command()
async def hug(ctx):
    random_hug = random.choice(jdata['hug'])
    await ctx.channel.purge(limit=1)
    await ctx.send(content=random_hug)


@bot.command()
async def gan(ctx):
    random_gan = random.choice(jdata['gan'])
    await ctx.send(content=random_gan)


@bot.command()
async def cat(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('叭噗')


@bot.command()
async def liver(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('肝有兩顆!')


@bot.command()
async def sad(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('嗷嗷')


@bot.command()
async def pink(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('破腦噁男')


@bot.command()
async def velon(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('魔法！')


@bot.command()
async def cute(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('???????????????????')


@bot.command()
async def sorry(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('對ㄅ起')


@bot.command()
async def test(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('test')


@bot.command()
async def gg(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('\\\|/')


@bot.command()
async def re(ctx, msg):
    await ctx.message.delete()
    await ctx.send(msg)


@bot.command()
async def delete(ctx, num: int):
    await ctx.channel.purge(limit=num + 1)
    await ctx.send('已刪除訊息')


@bot.command(pass_context=True)
async def roll(ctx, num1: float, num2: float):
    if num1 < num2:
        await ctx.send(random.uniform(num1, num2))
    else:
        await ctx.send(random.uniform(num2, num1))


@bot.command()
async def sexdog(ctx):
    random_sex = random.choice(jdata['sex'])
    await ctx.channel.purge(limit=1)
    await ctx.send(content=random_sex)


@bot.command()
async def tod(ctx, num: int):
    num1 = random.randint(1, num)
    num2 = random.randint(1, num)
    while num != 1 and num1 == num2:
        num1 = random.randint(1, num)
        num2 = random.randint(1, num)
    await ctx.send('問的人是:{0:2d}\n被禍害的人是:{1:2d}'.format(num1, num2))


if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run('NjgwMzczMjk1MTA2ODgzNjA5.XxRsOw.GxvgFRzH7mwEKvz59nHK_XRck8U')
