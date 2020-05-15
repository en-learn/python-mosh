# Functions
def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(increment(2, 3))

numbers = [1, 2, 3]  # list
number_tuple = (1, 2, 3)  # immutable

# keyword arguments
print(increment(2, by=3))

# defult parameters
print(increment(2))
