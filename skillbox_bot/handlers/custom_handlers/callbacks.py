from keyboards.inline.inline_keyboards import gen_inline_markup
from loader import bot
from states.mystates import CustomSearch
from utils.api import get_high_product, get_low_product
from utils.methods import serialize_data
from skillbox_bot.handlers.custom_handlers.custom_handler import get_custom_product
from skillbox_bot.handlers.custom_handlers.low_or_high_handler import get_product


@bot.callback_query_handler(func=lambda call: True)
async def callback_query(call):
    if "_/high_category" in call.data:
        call_data_in_list = call.data.split('_')
        result = await get_high_product(int(call_data_in_list[0]))
        for data in result:
            str_for_answer = serialize_data(data)
            await bot.send_message(call.message.chat.id, str_for_answer)

        await bot.send_message(call.message.chat.id, "Чем я могу помочь еще?", reply_markup=gen_inline_markup())

    elif "_/low_category" in call.data:
        call_data_in_list = call.data.split('_')
        result = await get_low_product(int(call_data_in_list[0]))

        for data in result:
            str_for_answer = serialize_data(data)
            await bot.send_message(call.message.chat.id, str_for_answer)

        await bot.send_message(call.message.chat.id, "Чем я могу помочь еще?", reply_markup=gen_inline_markup())

    elif "_/custom_category" in call.data:
        await bot.set_state(call.from_user.id, CustomSearch.price_range, call.message.chat.id)

        await bot.send_message(call.message.chat.id, "Введите диапазон цен в формате\n"
                                                     "цена от-цена до (Например: 5000-15000)")

        call_data_in_list = call.data.split('_')
        async with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
            data['category'] = int(call_data_in_list[0])



    elif call.data == "low":
        await get_product(call.message, '/low')

    elif call.data == "high":
        await get_product(call.message, '/high')

    elif call.data == "custom":
        await get_custom_product(call.message, '/custom')
