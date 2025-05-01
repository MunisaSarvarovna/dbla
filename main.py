import asyncio
import logging
import sys
from os import getenv
from email.charset import add_alias

from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
from aiogram.utils.deep_linking import create_start_link

from db import load, write
from database import add_user

TOKEN = "7502443242:AAGYUJuvwQONatmVqDSQ1zq2hjpzuZRzn2w"
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))



dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message, command: CommandObject) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    try:
        add_user(message.from_user.id)
    except:
        await message.answer("siz avval start bosgansiz")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

    data = load()
    data[str(message.from_user.id)] = 0
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    chat_id = command.args
    if chat_id:
        old_cnt = data.get(chat_id, 0)
        data[chat_id] = old_cnt + 1
        await message.answer(f"Siz quyidagi userga ref olgasiz {chat_id}")
    write(data)



@dp.message(F.text == "referat")
async def food_menu_handler(message: Message):
    await message.answer(text="Quyidagilardan birini tanlang:", reply_markup=main_menu)

@dp.message(F.text == "referat2")
async def food_menu_handler(message: Message):
    await message.answer(text="Quyidagilardan birini tanlang:", reply_markup=main_menu)


@dp.message(Command("refer"))
async def echo_handler(message: Message) -> None:
    link = await create_start_link(bot=bot, payload=str(message.from_user.id))
    await message.answer(link)

@dp.message(Command("count"))
async def echo_handler(message: Message) -> None:
    data = load()
    chat_id = str(message.from_user.id)

    await message.answer(f"{data.get(chat_id, 0)}")

async def main() -> None:

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())