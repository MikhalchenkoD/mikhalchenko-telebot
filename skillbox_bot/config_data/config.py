import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

ROOT_DIR = os.path.dirname(os.path.abspath('__main__'))
DATABASE = os.path.join(ROOT_DIR, 'database', 'history.db')
BOT_TOKEN = os.getenv("BOT_TOKEN")
DEFAULT_COMMANDS = (
    ('start', 'Запустить бота'),
    ('help', 'Вывести справку'),
    ('low', 'Вывести обувь по возрастанию'),
    ('high', 'Вывести обувь по убыванию'),
    ('custom', 'Вывести обувь по кастомным настройкам')
)
