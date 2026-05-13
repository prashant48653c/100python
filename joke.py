from pyjokes import get_joke

# This code uses the pyjokes library to fetch and print a random joke.
'''
def tell_joke():
    joke = get_joke()
    print(joke)


print("Here\"s a joke for you:")
tell_joke()

'''

print("What are you doing", "are you fine", sep="*", end="!!!\n")
print("What are you doing", "are you fine", sep="*", end="!!!\n")

a=323
b="Prashant"
c=None

print ( type(a), type(b), type(c) )

list1 = [1, 2, 3, 4, 5,"haha"]
print ( list1[0], list1[4] )
tuple1 = (1, 2, 3, 4, 5,"haha")
# tuple1[0] = 10 # This will raise an error because tuples are immutable  
print ( tuple1[0], tuple1[4] )
dict1 = {"name": "Prashant", "age": 30, "city": "New York"}
print ( dict1["name"], dict1["age"] )
set1 = {1, 2, 3, 4, 5,"haha"} # all should be unique and unordered
print ( set1 )

print(4534 // 50)
print(4534 / 50)


num=input("Enter a number: ")
print("You entered:", num)
print("The type of the input is:", type(num))
print("The type of the input is:", type(int(num)))