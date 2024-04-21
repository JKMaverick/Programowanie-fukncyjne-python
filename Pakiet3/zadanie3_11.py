def find_max_min_diff(lst):
    if not lst: 
        return None
    return max(lst) - min(lst) 

numbers = [10, 4, 5, 24, 6, 1, 3]
diff = find_max_min_diff(numbers)
print("Różnica między maksymalną a minimalną wartością:", diff)