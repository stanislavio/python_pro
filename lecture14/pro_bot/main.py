import os

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandStart, Command
from aiogram.types import Message, ParseMode
from aiogram.utils.markdown import hbold

from dotenv import load_dotenv

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(TOKEN)
# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher(bot)


@dp.message_handler(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`

    print(message.__dict__)

    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message_handler(Command(commands=('help', 'h', 'help_me')))
async def say_hello(message: types.Message):
    result = hello()
    await message.answer(f'HEllo, my friend, {result}')


@dp.message_handler()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


def hello():
    return 'hello'


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

"""
SELECT * from users
WHERE name = '1223' and surname like '%sdnls%'
ORDER BY name

"""

"""
query(User).filter(User.name='dfds', User.surname.like('%njlcds%').order_by(User.name)
"""