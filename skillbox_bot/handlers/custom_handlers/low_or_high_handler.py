from keyboards.inline.inline_keyboards import category_inline_markup
from loader import bot
from utils.api import get_all_category



@bot.message_handler(commands=['high', 'low'])
async def get_product(message, type_of_sorting=None):
    category_list = await get_all_category()

    if not type_of_sorting:
        type_of_sorting = message.text.split()[0]

    await bot.send_message(message.chat.id, "Выберите категорию по которой будем искать",
                           reply_markup=category_inline_markup(category_list, type_of_sorting))

