# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем LibreOffice
RUN apt-get update \
    && apt-get install -y --no-install-recommends libreoffice

# Устанавливаем python-docx и pytz
RUN pip install python-docx pytz

# Создаем рабочую директорию
WORKDIR /app

# Создаем необходимые директории внутри контейнера
RUN mkdir -p /app/template_doc
RUN mkdir -p /app/result_doc
RUN mkdir -p /app/result_pdf
RUN mkdir -p /app/logs
RUN mkdir -p /app/utils 

# Копируем исходный код Python программы и дополнительные файлы в контейнер
COPY pdf_generator.py /app
COPY utils/logger_config.py /app/utils/
COPY template_doc/ /app/template_doc/

# Команда для запуска Python скрипта
CMD ["python", "pdf_generator.py"]
