# Импорт необходимых библиотек
import threading
import time


class Multi_threading:
    
    def __init__(self):
        self.threads = []
    
    # Функция, имитирующая процесс
    def callback(self):
        for i in range(1, 51):
            time.sleep(2)
    
    # Функция, обновляющая прогресс обработки
    def monitoring(self):
        for i in range(1, 51):
            print(f'{i}/50')
            time.sleep(2)
    
    # Создание потоков 
    def making_threads(self):

        print('Запуск процесса:')

        # Поток, в котором выполняется основная обработка
        thread = threading.Thread(target=self.callback)
        thread.start()
        self.threads.append(thread)
        
        # Поток, в котором выполняется отображение прогресса
        thread_progress = threading.Thread(target=self.monitoring)
        thread_progress.start()
        self.threads.append(thread_progress)
        
        # Ждем завершения всех потоков
        for t in self.threads:
            t.join()
        
        print("Процесс завершен.")
    

if __name__ == "__main__":
    process = Multi_threading()
    process.making_threads()