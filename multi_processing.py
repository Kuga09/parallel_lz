# Импорт необходимых библиотек
import multiprocessing
import time
import math


class Multi_processing:
    
    def __init__(self, num_processes):
        self.num_processes = num_processes
    
    # Функция, вычисляющая факториал
    def calculate_factorial(self,data_chunk):
        return [math.factorial(x) for x in data_chunk]
    
    # Функция, разделения данных
    def split_data(self, data, num_parts):
        n = len(data)
        chunk_size = math.ceil(n / num_parts)
        return [data[i*chunk_size : min((i+1)*chunk_size, n)] 
                for i in range(num_parts)]
    
    # Синхронное вычисление
    def calculate_sync(self, data):
        start = time.time()
        sync_results = [math.factorial(x) for x in data]
        sync_time = time.time() - start
        return sync_results, sync_time
    
    # Многопроцессорное вычисление
    def calculate_parallel(self, data):
        start = time.time()
        
        # Разделение данных на части
        chunks = self.split_data(data, self.num_processes)
        
        # Многопроцессорное вычисление
        with multiprocessing.Pool(processes=self.num_processes) as pool:
            chunk_results = pool.map(self.calculate_factorial, chunks)
            parallel_results = [item for chunk in chunk_results for item in chunk]
        
        execution_time = time.time() - start
        return parallel_results, execution_time
    
    def results_of_comparison(self, data):
    
        # Синхронное вычисление
        sync_results, sync_time = self.calculate_sync(data)
        
        # Многопроцессорное вычисление
        parallel_results, mp_time = self.calculate_parallel(data)
        
        # Вывод результатов
        print(f"Синхронное вычисление: {sync_time:.4f} сек")
        print(f"Многопроцессорное вычисление: {mp_time:.4f} сек")
        print(f"Адрес в ячейке памяти на результаты: {hex(id(parallel_results))}")
        

if __name__ == "__main__":
    data = list(range(1, 501))
    process = Multi_processing(20)
    process.results_of_comparison(data)