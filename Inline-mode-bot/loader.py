from aiogram import Bot, Dispatcher
from data import config
from baza.sqlite import Database

ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS

bot = Bot(TOKEN)
db = Database(path_to_db="main.db")
dp = Dispatcher()