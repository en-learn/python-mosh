# For..Elase
names = ["John", "Mary"]

# Other programming languages
found = False
for name in names:
    if name.startswith("J"):
        print("Found")
        found = True
        break

if not found:
    print("Not found")

# Python
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")

