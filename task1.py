#Потрібно розробити програму, яка імітує приймання й обробку заявок: 
#програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними), 
#додавати їх до черги, а потім послідовно видаляти з черги для "обробки", імітуючи таким чином роботу 
#сервісного центру.

import queue
import threading
import time
import random

# Створення черги заявок
request_queue = queue.Queue()

# Генерація унікального ідентифікатора для кожної заявки
def generate_request_id():
    return random.randint(1000, 9999)

# Функція для створення та додавання нових заявок до черги
def generate_request():
    while True:
        request_id = generate_request_id()  # Створення унікального ідентифікатора
        request_queue.put(request_id)  # Додавання заявки до черги
        print(f"Заявка {request_id} додана до черги.")
        time.sleep(random.uniform(1, 3))  # Імітація часу до наступної заявки

# Функція для обробки заявок з черги
def process_request():
    while True:
        if not request_queue.empty():
            request_id = request_queue.get()  # Видалення заявки з черги
            print(f"Обробка заявки {request_id}...")
            time.sleep(random.uniform(2, 5))  # Імітація часу обробки заявки
            print(f"Заявка {request_id} оброблена.")
            request_queue.task_done()  # Відзначення обробки заявки
        else:
            print("Черга пуста.")
            time.sleep(1)  # Пауза, щоб перевірити чергу знову

# Запуск потоків для генерування та обробки заявок
generate_thread = threading.Thread(target=generate_request)
process_thread = threading.Thread(target=process_request)

generate_thread.start()
process_thread.start()

generate_thread.join()
process_thread.join()
