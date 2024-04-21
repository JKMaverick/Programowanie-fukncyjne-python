def filter_long_words(strings):
    average_length = sum(len(s) for s in strings) / len(strings) 
    return [s for s in strings if len(s) > average_length]  

string_list = ["hello", "world", "Python", "is", "awesome"]
filtered_list = filter_long_words(string_list)

print("Oryginalna lista:", string_list) 
print("Filtrowana lista:", filtered_list)