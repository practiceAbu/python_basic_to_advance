#Normal Function
def greet():
    print("Hello Good Morning")
greet()

#Function with one argument
name = input()
def greetWithName(name):
    print(f'Hello {name} how are you')
greetWithName(name)

# Function with multiple argument
def power(base,exponent =2):
    result = base ** exponent
    return result
print(power(3))
print(power(3,4))