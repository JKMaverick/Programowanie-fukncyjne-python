def rotate_list(lst, steps):
    if not lst:
        return []
    steps = steps % len(lst) 
    return lst[-steps:] + lst[:-steps] 

my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(my_list, 2)
print("Obrócona lista:", rotated_list)