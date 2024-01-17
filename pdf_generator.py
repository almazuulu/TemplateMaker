import io
import os
import subprocess
from docx import Document
from datetime import datetime
import pytz
from utils import logger_config
import logging


logger_config.setup_logging()


def create_pdf_from_docx_template(template_path, new_content, output_pdf_folder):
    logging.info("Начало создания PDF из шаблона DOCX")

    # Создаем документ в памяти
    doc = Document(template_path)

    # Добавляем новый контент
    for content in new_content:
        doc.add_paragraph(content)
    logging.info("Контент добавлен в документ")

    # Сохраняем DOCX в потоке байтов
    docx_stream = io.BytesIO()
    doc.save(docx_stream)
    docx_stream.seek(0)
    logging.info("DOCX файл создан в памяти")

    # Получаем текущую дату и время в часовом поясе Москвы
    msk_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(msk_tz).strftime("%d%m%Y_%H%M")
    output_pdf_path = os.path.join(output_pdf_folder, f"report_{current_time}.pdf")
    logging.info(f"Имя выходного файла PDF: {output_pdf_path}")

    # Создаем временный DOCX файл
    temp_docx = "temp.docx"
    with open(temp_docx, "wb") as f:
        f.write(docx_stream.getbuffer())
    logging.info("Временный DOCX файл создан")

    # Конвертируем DOCX в PDF
    try:
        subprocess.run([
            'libreoffice', '--headless', '--convert-to', 'pdf', '--outdir',
            output_pdf_folder, temp_docx
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info("Конвертация в PDF выполнена успешно")
    except Exception as e:
        logging.error(f"Ошибка при конвертации в PDF: {e}")

    # Переименовываем созданный PDF файл
    temp_pdf = os.path.join(output_pdf_folder, 'temp.pdf')
    os.rename(temp_pdf, output_pdf_path)
    logging.info("PDF файл переименован")

    # Удаляем временный DOCX файл
    os.remove(temp_docx)
    logging.info("Временный DOCX файл удален")

    return output_pdf_path


# Основной блок скрипта
if __name__ == "__main__":
    template_path = 'template_doc/template.docx'
    output_pdf_folder = 'result_pdf'
    new_content = [
        'Это первый абзац нового содержания.',
        'Это второй абзац нового содержания.'
    ]

    if not os.path.exists(output_pdf_folder):
        os.makedirs(output_pdf_folder)
        logging.info("Папка для PDF создана")

    output_pdf_path = create_pdf_from_docx_template(template_path, new_content,
                                                    output_pdf_folder)

    logging.info(f"Конвертация завершена. Проверьте файл: {output_pdf_path}")
