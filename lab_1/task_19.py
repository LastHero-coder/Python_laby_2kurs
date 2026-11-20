# ==========================================
# 1. САМ ДЕКОРАТОР
# ==========================================
def cache(func):
    # Создаем пустой словарь. Это и есть наш "кэш" (блокнот с ответами)
    saved_results = {}

    def wrapper(*args, **kwargs):
        # args — это кортеж, например (5, 10). Он подходит для ключа словаря.
        key = args

        # Проверка на существование ключа в словаре
        if key in saved_results:
            print(f"   ИЗ КЭША Взяли готовый ответ для аргументов: {args}")
            return saved_results[key]  

        
        print(f"   ВЫЧИСЛЯЕМ Функция работает... аргументы: {args}")
        result = func(*args, **kwargs)

        saved_results[key] = result

        return result

    return wrapper

####################################################
@cache
def slow_calculation(a, b):
    print(" Внимание! Выполняется сложная математика! ")
    return a + b



print("--- Первый вызов ---")
print("Результат:", slow_calculation(5, 10))

print("\n--- Второй вызов (те же числа) ---")
print("Результат:", slow_calculation(5, 10))

print("\n--- Третий вызов (другие числа) ---")
print("Результат:", slow_calculation(2, 3))