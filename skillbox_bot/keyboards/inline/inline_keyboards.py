from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_inline_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Вывести обувь по возрастанию", callback_data="low"),
        InlineKeyboardButton("Вывести обувь по убыванию", callback_data="high"),
        InlineKeyboardButton("Вывести обувь по кастомным настройкам", callback_data="custom"),
    )

    return markup


def category_inline_markup(category_list, type_of_sorting):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for category in category_list:
        markup.add(
            InlineKeyboardButton(category['title'], callback_data=f"{category['id']}_{type_of_sorting}_category"))

    return markup
