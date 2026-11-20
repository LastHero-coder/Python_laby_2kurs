import time

def timing(func):

    def wrapper(*args, **kwargs):
        # 1. Засекаем время СТАРТ
        start = time.time()
        
        # 2. Выполняем нашу функцию
        result = func(*args, **kwargs)
        
        # 3. Засекаем время ФИНИШ
        end = time.time()
        
        # 4. Считаем разницу в миллисекундах (умножаем на 1000)
        milliseconds = (end - start) * 1000
        
        print(f"Время работы: {milliseconds:.2f} мс")
        
        return result
        
    return wrapper



@timing
def slow_function():
    time.sleep(0.5)
    return "Готово"

slow_function()