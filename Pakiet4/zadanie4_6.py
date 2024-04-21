def map_list(lst, func):
    return [func(x) for x in lst]

print(map_list([1, 2, 3, 4], lambda x: x * 2)) 