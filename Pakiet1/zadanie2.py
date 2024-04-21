def make_multiplier(x):
    def multiply(n):
        return x*n

    return multiply

double = make_multiplier(2)
print(double(2))
