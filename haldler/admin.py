from aiogram import types, Dispatcher
from config import bot
from config import ADMINS
import random

async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id  not in ADMINS:
          await message.answer("Вы не  являетесь   админом  , к сожалению не имейте права")
         elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f"{message.from_user.first_name} братан кикнул "
                                 f"{message.reply_to_message.from_user.full_name}")

    else:
        await message.answer("Пиши в группе!")


async def dice(message: types.Message):
    if message.from_user.id == 'ADMIN':
        games = ['🎰', '🎳', '🎲', '🏀']
        if message.text.startswith('game'):
            await bot.send_dice(message.chat.id, random.choice(games))




def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(dice, commands=['game'])


