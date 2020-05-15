# Scope
message = "a"

def greet():
    global message
    message = "b"
    print(message)

greet()
print(message)

