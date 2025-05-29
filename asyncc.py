# Импорт необходимых библиотек
import asyncio


class Asynс:

    def __init__(self):
        self.delay = 3

    # Асинхронная функция с задержкой и исключением
    async def task_error(self):

        await asyncio.sleep(self.delay)
        raise ValueError("Что-то пошло не так!")

    # Функция, обрабатывающая исключение
    async def handler(self):

        print("Запуск процесса")

        try:
            result = await self.task_error()
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка")

        print("Программа завершена")



if __name__ == "__main__":
    process = Asynс()
    asyncio.run(process.handler())
