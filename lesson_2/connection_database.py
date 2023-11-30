import asyncio
import logging
import sys
from aiogram import Bot , Dispatcher, types , F
from aiogram.filters.command import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from geopy.distance import geodesic

BOT_TOKEN = "6911994795:AAEpgovKx1eTq2yIVIKgXmHW0HIt4eB2RP4"
dp = Dispatcher()

def buttons():
   btn1 = KeyboardButton(text="btn1")
   btn2 = KeyboardButton(text="btn2")
   btn3 = KeyboardButton(text="btn3")
   design = [
       [btn1,btn2,btn3]
   ]
   return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

@dp.message(CommandStart())
async def start_handlering(msg: types.Message):
     await msg.answer("Hello", reply_markup=buttons())



async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
