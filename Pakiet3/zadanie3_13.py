def split_list(lst, length):
    return [lst[i:i+length] for i in range(0, len(lst), length)]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
split_lists = split_list(my_list, 3)
print("Podzielona lista:", split_lists)