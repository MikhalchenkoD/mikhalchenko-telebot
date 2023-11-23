from loader import bot
from keyboards.inline.inline_keyboards import gen_inline_markup


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.send_message(message.chat.id, "Привет, я бот магазина обуви и вот что я могу", reply_markup=gen_inline_markup())
