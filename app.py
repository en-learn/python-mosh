# FizzBuzz
def fizz_buzz(input):
    result = ""
    if input % 3 == 0:
        result += "Fizz"
    if input % 5 == 0:
        result += "Buzz"
    return result or input


# print(fizz_buzz(1))
# print(fizz_buzz(3))
# print(fizz_buzz(5))
# print(fizz_buzz(15))

for number in range(0, 101):
    print(fizz_buzz(number))
