import time


print(time.time()) # in millisecond since 1 Jan 1970
print(time.ctime()) # current time in human readable format
print(time.localtime()) # current time in struct_time format
print(time.strftime("%Y-%m-%d %H:%M:%S")) # format current

print(time.sleep(2)) # sleep for 2 seconds, it waits for 2 seconds before executing the next line
print("Awake now!")


# match statement in python 3.10 and above
x = 1
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")

for i in range(5): # 0 to 4
    print(i)

for i in range(1, 5): # 1 to 4
    print(i)

for i in range(1, 101,10): # 1 to 100 but space between 10 numbers
    print(i)

print("Even numbers from 0 to 10:")
while x < 5:
    print(x)
    x += 1

    if x == 3:
        continue
    if x==4:
        break
