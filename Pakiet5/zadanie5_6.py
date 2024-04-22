def filter_a_words(words):
    return list(filter(lambda x: x.startswith('a'), words))


def square_numbers(numbers):
    return list(map(lambda x: x ** 2, numbers))


print(filter_a_words(["apple", "banana", "avocado", "cherry"]))
print(square_numbers([1, 2, 3, 4]))