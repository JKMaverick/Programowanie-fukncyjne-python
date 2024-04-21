from collections import Counter
def most_common(lst):
    return Counter(lst).most_common(1)[0][0]

print(most_common([1, 2, 3, 2, 4, 2, 3, 2, 2, 5]))