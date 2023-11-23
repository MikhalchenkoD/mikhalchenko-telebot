from loader import bot
from .mystates import CustomSearch
from utils.api import get_custom_product
from utils.methods import serialize_data


@bot.message_handler(state=CustomSearch.quantity, is_digit=True)
async def ready_for_answer(message):
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        result = await get_custom_product(data['category'], data['price_range'], message.text)

        for i in result:
            str_for_answer = serialize_data(i)
            await bot.send_message(message.chat.id, str_for_answer)

    await bot.delete_state(message.from_user.id, message.chat.id)