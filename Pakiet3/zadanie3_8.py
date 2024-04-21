def partition_list(lst, condition_func):
    true_list, false_list = [], []
    for item in lst:
        if condition_func(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return true_list, false_list

my_list = [1, 2, 3, 4, 5, 6]
even_list, odd_list = partition_list(my_list, lambda x: x % 2 == 0)
print("Elementy parzyste:", even_list)
print("Elementy nieparzyste:", odd_list)