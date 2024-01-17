import subprocess
from docx import Document
import os


def add_content_to_docx(template_path, new_content, output_path):
    # Загрузка шаблона DOCX
    doc = Document(template_path)

    # Добавление нового содержимого
    for content in new_content:
        doc.add_paragraph(content)

    # Сохранение изменённого документа
    doc.save(output_path)


def convert_to_pdf(input_path, output_folder):
    # Команда для конвертации файла в PDF с помощью LibreOffice
    command = [
        'libreoffice', '--headless', '--convert-to', 'pdf', '--outdir',
        output_folder, input_path
    ]

    # Выполнение команды
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


# Путь к шаблону DOCX
template_path = 'template_doc/template_test.docx'

# Путь к выходному файлу DOCX
output_docx_path = 'result_doc/my_document.docx'

# Содержимое для добавления в документ
new_content = [
    'Это первый абзац нового содержания.',
    'Это второй абзац нового содержания.'
]

# Добавляем контент в DOCX
add_content_to_docx(template_path, new_content, output_docx_path)

# Папка для сохранения PDF
output_pdf_folder = 'result_pdf'

# Убедитесь, что папка для PDF существует
if not os.path.exists(output_pdf_folder):
    os.makedirs(output_pdf_folder)

# Конвертируем в PDF
convert_to_pdf(output_docx_path, output_pdf_folder)

print("Конвертация завершена. Проверьте папку PDF.")
