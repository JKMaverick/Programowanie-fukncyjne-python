def map_tuples(lst, func):
    return [func(*tpl) for tpl in lst]

print(map_tuples([(1, 2), (3, 4)], lambda x, y: x * y)) 