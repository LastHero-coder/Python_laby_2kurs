def unique_elements(nested_list):
    result = []  # Список для уникальных чисел
    
    # копия списка чтобы случайно не изменить оригинал
    # Это наша "очередь" элементов, которые нужно проверить
    queue = nested_list.copy() 

    while queue:
        item = queue.pop(0)

        if type(item) == list:
            # Мы "распаковываем" его и добавляем его содержимое в начало очереди
            queue = item + queue
        else:
            # провепка, уже нет в результате?
            if item not in result:
                result.append(item)
                
    return result


list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]

print("Исходный список:", list_a)
print("Результат:", unique_elements(list_a))