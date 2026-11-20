def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            for i in range(len(args)):
                if not isinstance(args[i], expected_types[i]):
                    raise TypeError(f"Ошибка! Аргумент {args[i]} не того типа.")
            
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    return a + b

print(add(5, 10))   # Сработает, выведет 15
print(add(5, "10")) # Выдаст ошибку TypeError