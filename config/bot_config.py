from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
import logging

config = dotenv_values("./config/.env")
API_TOKEN = config["API_TOKEN"]
ADMIN = config["ADMIN"]


logging.basicConfig(level=logging.INFO) #set logging level

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

