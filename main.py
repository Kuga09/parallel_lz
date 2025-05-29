# Имрот необходимых модулей и библиотек
from multi_threading import Multi_threading
from multi_processing import Multi_processing
from asyncc import Asynс
import asyncio


# Функция main
def main():
    user_input=input('Какой алгоритм вы хотите использовать:\n'
    '1 — Многопоточность\n'
    '2 — Многопроцессорность\n' 
    '3 — Асинхрон\n')
    if user_input == '1':
        process = Multi_threading()
        process.making_threads()
    elif user_input == '2':
        data = list(range(1, 501))
        process = Multi_processing(20)
        process.results_of_comparison(data)
    elif user_input == '3':
        process = Asynс()
        asyncio.run(process.handler())
    
    
if __name__ == '__main__':
    main()