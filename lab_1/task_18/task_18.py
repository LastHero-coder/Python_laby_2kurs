import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = str(datetime.datetime.now())
            func_name = func.__name__
            
            log_text = f"Время: {now} | Функция: {func_name} | args: {args} | kwargs: {kwargs}\n"
            
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(log_text)
                
            return func(*args, **kwargs)
        return wrapper
    return decorator


MY_PATH = r"C:\Users\HP\Desktop\VUZ_\codY_\Python_labs_2kurs_\lab_1\task_18\log.txt"

@log_calls(MY_PATH) 
def calculate_sum(a, b):
    return a + b

print("Результат:", calculate_sum(5, 10))