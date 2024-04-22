from functools import reduce

def find_max(lst):
    return reduce(lambda a, b: a if a > b else b, lst)

def calculate_average(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)

numbers = [1, 2, 3, 4, 5, 6]
print(find_max(numbers))
print(calculate_average(numbers))