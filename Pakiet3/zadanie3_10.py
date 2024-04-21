def cumulative_sum(lst):
    cumulative_list = []
    total = 0
    for item in lst:
        total += item
        cumulative_list.append(total)
    return cumulative_list

numbers = [1, 2, 3, 4, 5]
cum_sum = cumulative_sum(numbers)
print("Suma skumulowana:", cum_sum)