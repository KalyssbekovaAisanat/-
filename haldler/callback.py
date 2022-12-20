from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp



#@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):

    question = "Что означает «www» в браузере веб-сайтов?"
    answers = [
        "Всемирная паутина",
        "Адрес сайтов",
        "База данные сети"
        ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        open_period=10,
    )

async def quiz_3(call: types.CallbackQuery):

    question = "каком году первые создал python"
    answers = [
        "1991",
        "1990",
        "1992"
        ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        open_period=10,
    )





def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")