# Function using 1 iteration
def one_iteration(a, b):
    return a * b


# Function using N iterations
def n_iteration(a, b):
    result = 0

    for i in range(b):
        result = result + a

    return result


# Values
a = 5
b = 6


# Printing results
print("1 iteration:", one_iteration(a, b))
print("N iteration:", n_iteration(a, b))