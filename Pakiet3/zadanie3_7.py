def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

nested_list = [1, [2, 3], [4, [5, [6, 7]]], 8]
flat_list = flatten_list(nested_list)

print("Zagnieżdżona lista:", nested_list)
print("Spłaszczona lista:", flat_list)