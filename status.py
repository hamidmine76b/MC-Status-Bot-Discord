### Made By Hamidmine76b
import discord
import requests
import asyncio
from discord.ext import commands

TOKEN = 'Your Bot Token'  # توکن خود را اینجا قرار دهید
SERVER_IP = 'Your Miencraft Server Ip' # آیپی سرور ماینکرفتی خود را اینجا قرار دهید

intents = discord.Intents.all()

# ایجاد شیء Bot با intents
bot = commands.Bot(command_prefix='!', intents=intents)

async def update_status():
    while True:
        try:
            # درخواست به API mcstatus.io برای دریافت وضعیت سرور
            response = requests.get(f'https://api.mcstatus.io/v2/status/java/{SERVER_IP}')
            if response.status_code == 200:
                data = response.json()
                players = data['players']['online']  # تعداد پلیرها را از پاسخ دریافت کنید
                max_players = data['players']['max']  # حداکثر تعداد پلیرها
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{players}/{max_players} Players 🎮"))
            else:
                # اگر سرور آفلاین باشد
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Server is offline ❌"))
        except Exception as e:
            # در صورت بروز خطا (مثلاً سرور آفلاین است)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Server is offline ❌"))
            print(f"An error occurred: {e}")

        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await update_status()

# اجرای بات
bot.run(TOKEN)
