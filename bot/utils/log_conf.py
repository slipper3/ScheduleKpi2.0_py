import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    # Створення головного логера, якщо його ще не існує
    if not logging.getLogger().handlers:
        # Налаштування логування
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)

        # Додавання обробника для запису логів у файл
        file_handler = RotatingFileHandler('bot_log.txt', maxBytes=1*1024*1024, backupCount=5)
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Відфільтрувати логи aiogram для рівня INFO
        aiogram_logger = logging.getLogger('aiogram')
        aiogram_logger.setLevel(logging.WARNING)

    # Повернення логера
    return logging.getLogger(__name__)