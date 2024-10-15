import os
import shutil
import time
from datetime import datetime
import threading
import stopit

user_input = ''

def get_input():
    global user_input
    user_input = input("Введите 'exit' для выхода, чтобы продолжить нажмите любую клавишу или подождите\n")
def timed_input(timeout):
    global user_input
    user_input = ''
    thread = threading.Thread(target=get_input)
    thread.start()
    thread.join(timeout - 0.1)
    return user_input

def backup():
    src = input("Введите путь к директории для резервного копирования: ")
    dst = input("Введите путь к директории для сохранения резервных копий: ")
    interval = int(input("Введите интервал времени (в секундах) между резервными копиями: "))
    if not os.path.exists(src):
        print("Исходная директория не найдена")
        return
    if not os.path.exists(dst):
        os.makedirs(dst)
        print(f"Целевая директория {dst} была создана.")

    print("Процесс копирования начался")

    try:
        while True:
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            backup_dst = os.path.join(dst, f'backup_{timestamp}')
            shutil.copytree(src, backup_dst)
            print(f"Резервная копия успешно создана в {backup_dst}")
            if timed_input(interval) == "exit":
                print("Цикл завершен.")
                break
            else:
                print("Тайм-аут или пустой ввод, продолжаем...")
            time.sleep(1)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


backup()