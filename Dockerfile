# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем LibreOffice
RUN apt-get update \
    && apt-get install -y --no-install-recommends libreoffice

# Устанавливаем python-docx
RUN pip install python-docx

# Создаем рабочую директорию
WORKDIR /app

# Создаем необходимые директории внутри контейнера
RUN mkdir -p /app/template_doc
RUN mkdir -p /app/result_doc
RUN mkdir -p /app/result_pdf

# Копируем исходный код Python программы и дополнительные файлы в контейнер
COPY pdf_generator.py /app
COPY template_doc/ /app/template_doc/

# Команда для запуска Python скрипта
CMD ["python", "pdf_generator.py"]
