import asyncio
import handlers
from telebot import asyncio_filters
from loader import bot
from utils.set_bot_commands import set_default_commands
import states

async def main():
    bot.add_custom_filter(asyncio_filters.StateFilter(bot))
    bot.add_custom_filter(asyncio_filters.IsDigitFilter())
    await set_default_commands(bot)
    await bot.polling()


if __name__ == "__main__":
    asyncio.run(main())
