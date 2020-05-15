# For Loops
# for x in "Python":
#     print(x)

# for x in ['a', 'b', 'c']:
#     print(x)

for x in range(5):
    print(x)

print("")

for x in range(3, 5):
    print(x)

print("")

for x in range(0, 10, 2):
    print(x)

# The range function does not return a list object
print(range(5))
print([1, 2, 3, 4, 5])

# A range takes very little memory, even if the range is large
print(type(range(5000000000)))
