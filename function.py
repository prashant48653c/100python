
def sayHi(name="Tori", greeting="Hello"):
    print(greeting + ", " + name + "!")


name=input("Enter your name: ")
sayHi(name=name, greeting="Hi")


# This creates tuple of arguments and we can unpack it in the function definition
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(add(1, 2, 3, 4, 5))