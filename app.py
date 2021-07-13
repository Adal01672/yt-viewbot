import selenium
from selenium.webdriver.chrome.options import Options
import random
import time
from selenium import webdriver
import discord
from discord.ext import commands
client=commands.Bot(command_prefix='boost ')
PROXY_list=["195.110.7.195:3121",
"183.87.153.98:49602",
"212.175.191.92:8080",
"85.216.127.182:8080",
"124.41.213.201:39272",
"167.99.206.6:3128",
"5.252.161.48:8080",
"102.129.255.223:80",
"150.129.115.118:48071",
"186.159.3.193:56861",
"103.11.106.70:8181",
"109.193.195.14:8080",
"79.143.87.138:9090",
"8.210.157.49:17309",
"103.130.141.98:8080",
"189.199.126.94:8080",
"109.193.195.6:8080",
"160.19.232.85:3128",
"188.68.52.45:80",
"109.193.195.8:8080",
"92.204.129.161:80",
"150.129.151.62:6666",
"118.70.109.148:55443",
"103.115.14.207:80",
"103.115.14.200:80",
"46.8.247.3:50967",
"190.217.1.121:32192",
"103.115.14.37:80",
"188.246.191.254:8081",
"13.235.137.56:8081",
]




@client.event
async def on_ready():
	print('ready')


@client.command()
async def yt(ctx,views,min_time,max_time,link):
	error=False
	views=int(views)
	min_time=int(min_time)
	max_time=int(max_time)
	if views > 20:
		error=True
		await ctx.send('sorry but you can not send more than 20 views at a time')
	elif min_time <0:
		error=True
		await ctx.send('sorry but you cant do cant do less than 0')
	elif min_time >60:
		error=True
		await ctx.send('sorry but you cant view for such a long time give chance to other to use the bot')
	elif max_time <0:
		error=True
		await ctx.send('sorry but you cant do cant do less than 0')
	elif max_time >60:
		error=True
		await ctx.send('sorry but you cant view for such a long time give chance to other to use the bot')
	elif min_time > max_time:
		error=True
	elif error==False:
		min_time=min_time-1
		max_time=max_time+1
		Time=random.randrange(min_time,max_time)
		chrome_options = webdriver.ChromeOptions()
		chrome_options.binary_location=os.getenviron.get(GOOGLE_CHROME_BIN)
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-dv-sh-usage')
		driver=webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'))
		await ctx.send(f'sending {views} views to this {link} video, Note: you will not get the view instantly because after the bot sents the view youtube is going to verify if the view is legit or not in this case it will be legit because the views are sent from random 22 proxies.')
		
		for i in range(views):
			randomize=random.choice(PROXY_list)
			chrome_options.add_argument('--proxy-server=%s' % randomize)
			driver.get(f'{link}')
			time.sleep(Time)
	driver.close()

client.run('ODYxOTMzNTgwMTA3NTEzODU2.YORAMw.PXLnRQ5hhdWXop_pw2pRUvAY0rk')
