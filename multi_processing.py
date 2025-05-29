import multiprocessing
import time
import math


def calculate_factorial(data_chunk):
    for x in data_chunk:
        return math.factorial(x)

def split_data(data, num_parts):
    n = len(data)
    chunk_size = math.ceil(n / num_parts)
    return [data[i*chunk_size : min((i+1)*chunk_size, n)] 
            for i in range(num_parts)]

if __name__ == "__main__": 
    data = list(range(1,501))
     
    # Синхронное вычисление
    start = time.time()
    result = calculate_factorial(data)
    sync_time = time.time() - start
    print(f"Синхронное вычисление: {sync_time:.5f} сек")

    # Многопроцессорное вычисление
    num_processes = 4
    start = time.time()
    
    # Надежное разделение данных
    chunks = split_data(data, num_processes)
    
    with multiprocessing.Pool(processes = num_processes) as pool:
        results = pool.map(calculate_factorial, chunks)
        result_parallel = sum(results)
    
    mp_time = time.time() - start
    print(f"Многопроцессорное вычисление: {mp_time:.5f} сек")
    print(f"Результаты совпадают: {result == result_parallel}")