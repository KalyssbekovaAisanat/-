from aiogram import Bot, Dispatcher
from decouple import config


TOKEN = config("TOKEN")
ADMINS = [ 1873812578]


bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)