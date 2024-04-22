def outer_function(text):
    global outer_var
    outer_var = "Jestem zmienną zewnętrzną"

    def inner_function(inner_text):
        return text + " " + inner_text

    return inner_function

func = outer_function("Witaj,")
print(func("świecie!"))