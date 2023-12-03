# Обновляет DATA из data.py. В коде начинает использоваться актуальная версия data.json.

import os
import sys
import subprocess

def restart_program():
    # Получаем путь к текущей папке
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Формируем путь к файлу data.py
    data_path = os.path.join(current_dir, '..', 'data.py')
    # Получаем путь к интерпретатору Python
    python = sys.executable
    # Запускаем новый процесс с файлом data.py
    subprocess.Popen([python, data_path])
    # Завершаем текущий процесс
    sys.exit()

# Вызываем функцию перезапуска
restart_program()
