
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

add(1, 2, 3, 4, 5)



# add as dictionary, we can unpack it in the function definition
def addasDict(**nums):
    total = 0
    for key, value in nums.items():
        total += value
    return total


print(addasDict(first=1, second=2, third=3, fourth=4, fifth=5))


list1 = [1, 2, 3, 4, 5,6,7,8,9,0]
print(len(list1)) # length of the list
print(max(list1)) # maximum value in the list
print(min(list1)) # minimum value in the list
print(sum(list1)) # sum of all values in the list


print(list1[:]) 
print(list1[0:5]) # slicing
print(list1[5:]) # slicing
print(list1[::2]) # slicing with step
if(1 in list1):
    print("1 is in the list")
else:
    print("1 is not in the list")


#Creating a list of squares using list comprehension 0 to 9

squares= [ x**2 for x in range(10) if x%2==0 ] # list comprehension with condition, it will create a list of squares of even numbers from 0 to 9
print(squares)

tuple1 = (1, 2, 3, 4, 5,"haha")
print ( tuple1[0], tuple1[4] )
for item in tuple1:
    print(item)