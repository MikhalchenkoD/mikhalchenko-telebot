from loader import bot
from skillbox_bot.states.mystates import CustomSearch


@bot.message_handler(state=CustomSearch.price_range)
async def ask_price(message):
    await bot.send_message(message.chat.id, "Введите кол-во товара, которое нужно найти")

    await bot.set_state(message.from_user.id, CustomSearch.quantity, message.chat.id)
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['price_range'] = message.text.split('-')
