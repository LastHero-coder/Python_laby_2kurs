def flatten_list(lst):  # Не забываем передать аргумент lst!
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            box = lst.pop(i)
            flatten_list(box)
            lst[i:i] = box
            i += len(box)
        else:
            i += 1

def main():
    list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
    flatten_list(list_a)
    print(list_a)

if __name__ == "__main__":
    main()