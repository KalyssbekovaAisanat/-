from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from keyboards.client_kb import start_markup

#@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Здраствуйте  {message.from_user.first_name}",
                           reply_markup=start_markup)
    #await message.answer("This is an answer method")
   # await message.reply("This is a reply method")


async def info_handler(message: types.Message):
     await message.reply("Cам разбирайся!")

#@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Самый большой стран мира?"
    answers = [
        'Китай',
        'Россия',
        'Канада',
        'США',
        'Индия',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Теперь будешь знать ))",
        open_period=10,
        reply_markup=markup
    )


#@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
   photo = open("medua/photo_2022-07-12_16-33-04.jpg", "rb")
   await bot.send_photo(message.chat.id, photo=photo)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler( quiz_1,commands=['quiz'])
    dp.register_message_handler( mem,commands=['mem'])
    dp.register_message_handler(info_handler, commands=['info'])