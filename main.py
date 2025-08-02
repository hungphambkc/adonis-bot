import os
import discord
from discord.ext import commands
import requests
import json
from keep_alive import keep_alive
from datetime import datetime
import pytz

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


def get_quote2():
  response = requests.get("https://api.quotable.io/random")
  json_data = json.loads(response.text)
  quote2 = json_data[0]['content'] + json_data[0]['author']
  return (quote2)


def get_now():
  tz_VN = pytz.timezone('Asia/Jakarta')
  now = datetime.now(tz_VN)
  d1 = now.strftime("%d/%m/%Y, %H:%M,%S")
  print("d1 =", d1)
  return (now)


def get_karnaugh():
  karnaugh = "https://www.charlie-coleman.com/experiments/kmap/"
  print("karnaugh = ", karnaugh)
  return (karnaugh)


def get_math():
  math = "https://matrixcalc.org/vi/slu.html#solve-using-Cramer%27s-rule%28%7B%7B12+i,3%2ai,-4%2ai,50%7D,%7B3%2ai,16+3%2ai,-8,0%7D,%7B-4%2ai,-8,10,0%7D%7D%29"
  print("math = ", math)
  return (math)


def get_perfekt():
  perfekt = "https://wetalent.edu.vn/danh-sach-cac-dong-tu-tieng-duc-di-voi-sein-o-perfekt/"
  print("perfekt = ", perfekt)
  return (perfekt)


def get_beam():
  beam = "https://beamguru.com/online/beam-calculator/"
  print("beam = ", beam)
  return (beam)


def get_lim():
  lim = "https://www.mathportal.org/calculators/calculus/limit-calculator.php"
  print("lim = ", lim)
  return (lim)


def get_integral():
  integral = "https://www.integral-calculator.com/"
  print("integral = ", integral)
  return (integral)


def get_derivative():
  derivative = "https://www.derivative-calculator.net/"
  print("derivative = ", derivative)
  return (derivative)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('!quote'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('!quote2'):
    quote2 = get_quote2()
    await message.channel.send(quote2)

  if message.content.startswith('!now'):
    now = get_now()
    await message.channel.send(now)

  if message.content.startswith('!karnaugh'):
    karnaugh = get_karnaugh()
    await message.channel.send(karnaugh)

  if message.content.startswith('!math'):
    math = get_math()
    await message.channel.send(math)

  if message.content.startswith('!perfekt'):
    perfekt = get_perfekt()
    await message.channel.send(perfekt)

  if message.content.startswith('!beam'):
    beam = get_beam()
    await message.channel.send(beam)

  if message.content.startswith('!lim'):
    lim = get_lim()
    await message.channel.send(lim)

  if message.content.startswith('!integral'):
    integral = get_integral()
    await message.channel.send(integral)

  if message.content.startswith('!derivative'):
    derivative = get_derivative()
    await message.channel.send(derivative)


keep_alive()

try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
  if e.status == 429:
    print(
        "The Discord servers denied the connection for making too many requests"
    )
    print(
        "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
    )
  else:
    raise e
