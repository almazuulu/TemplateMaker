import os
import datetime
import logging


def setup_logging():
    # Создаем директорию для логов, если она еще не существует
    log_directory = "logs"
    os.makedirs(log_directory, exist_ok=True)

    # Настройка логгирования
    log_filename = os.path.join(log_directory, 'conversion.log')
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()  # Для вывода логов в консоль также
        ]
    )
