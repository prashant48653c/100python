# formating python strings old way

letter= "Hey my name is {} and I am {} years old"

letter.format("Prashant", 30) # this will replace the {} with the values in the format function
print(letter.format("Prashant", 30))
print(letter)

# using f string
name = "Prashant"
age = 30
price= 5.3434
print(f"Hey my name is {name} and I am {age} {price:.2f} years old") # this will replace the {} with the values in the f string


# Docstring and Pep8
def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b

add(1, 2)
print(add.__doc__) # this will print the docstring of the function, should be below the function

#pep8
import this


#loop with else
for i in range(5):
    print(i)
    if i == 3:
        break

else:
    print("Loop is over")

