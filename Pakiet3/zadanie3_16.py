def remove_whitespace(string_list):
    return [s.strip() for s in string_list]

my_strings = ['  hello ', 'world!  ', '  python  ']
no_whitespace_list = remove_whitespace(my_strings)
print("Lista bez białych znaków:", no_whitespace_list)