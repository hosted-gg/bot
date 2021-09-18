import discord
import requests
from discord.ext import commands


bot = commands.Bot(command_prefix='ok ')
bot.remove_command("help")
cookie = {'sessionid': {'path': '/', 'value': '481795554'}}
html_tags = ['image', 'button', 'text', 'url']


async def request(query):
    resp = requests.post('https://icap.iconiq.ai/talk', data={'input': query, 'botkey': 'icH-VVd4uNBhjUid30-xM9QhnvAaVS3wVKA3L8w2mmspQ-hoUB3ZK153sEG3MX-Z8bKchASVLAo~', 'channel': '7', 'sessionid': '481795554', 'client_name': 'uuiprod-un18e6d73c-user-37911'})
    print(resp.content)
    return resp.json()


async def parse_resp(resp):
    for i in html_tags:
        resp = resp.replace(f'<{i}>', '').replace(f'</{i}>', ' ')
    return resp


@bot.command()
async def help(ctx):
    embed = discord.Embed(title='Help', description='Help command', colour=0xd10a07)
    embed.add_field(name='ok `kuki some request`', value='Use kuki assistant')
    embed.add_field(name='ok `kuki help`', value='Show this message')
    embed.add_field(name='ok `kuki invite`', value='Send a invite link')
    embed.set_author(name='Discuki, hosted by hosted-gg.xyz', icon_url='https://i.imgur.com/U9mSPNE.png', url='https://hosted-gg.xyz')
    embed.set_image(url='https://chat.kuki.ai/9cfcb64527413e9201cd553852745a2f.gif')
    await ctx.send(embed=embed)


@bot.command()
async def kuki(ctx, *req):
    req = ' '.join(req)
    if req == 'help':
        await help(ctx)
    elif req == 'invite':
        await ctx.send('https://discord.com/oauth2/authorize?client_id=888723983300694016&scope=bot&permissions=8')
    else:
        resp = await request(req)
        print(resp)
        for i in resp['responses']:
            resp_ = await parse_resp(i)
            await ctx.send(resp_)


bot.run('ODg4NzIzOTgzMzAwNjk0MDE2.YUW2tQ.PdFw4C3u1Bgia5RGs_R2wSRI6QY')