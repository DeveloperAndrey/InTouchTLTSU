import sqlite3
from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import KeyboardButton
from config import TOKEN
from Function import *
from cmdAdmin import *
 
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db = sqlite3.connect('database.db')
cur = db.cursor()
 
