# def greet():  # no return type/no argument
#     print("Hi")
#
#
# greet()
# def greet(name):  # no return type/with argument
#     print("Hi", name)
#
#
# greet("Ganishka")
# def greet(name="Gani"):  # no return type with default argument
#     print("Hi", name)
#
#
# greet()
# greet("Bharath")
# greet(name="Gowri")
def greet(a, b):  # return type with argument
    return a + b


result = greet(2, 4)
print(result)
