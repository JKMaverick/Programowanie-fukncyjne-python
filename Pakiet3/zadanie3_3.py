def recursive_sum(numbers):
    total_sum = 0
    for element in numbers:
        if isinstance(element, list):
            total_sum += recursive_sum(element)
        else:
            total_sum += element
    return total_sum

nested_list = [1, 2, [3, 4], [5, [6, 7]], 8]
total_sum = recursive_sum(nested_list)

print("Zagnieżdżona lista:", nested_list)
print("Suma wszystkich liczb:", total_sum)