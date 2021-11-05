import random

#Step 1: Input the random list
n = int(input("The number of list: "))
print("Enter the range [a,b] to random")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
randomlist = [random.randrange(a,b+1) for i in range(0,n)]
print("random list: ",randomlist)

#Step 2: Check the option of user
inputstring = "Enter the number need to find (" + str(a) +" =< x <= "+ str(b) +"): "
x = int(input(inputstring))
while (x < a) or (x > b):
    print("Input error. Please try again")
    x = int(input(inputstring))

#Step 3: Sort random list ascending order
for i in range(0,len(randomlist)-1):
    for j in range(i+1,len(randomlist)):
        if randomlist[i] > randomlist[j]:
            randomlist[i],randomlist[j] = randomlist[j],randomlist[i]
print("List after sort ascending order: ",randomlist)

#Step 4: Find the number
countloopstep = 0
count = 0
positionlist = []
for i in range(0,len(randomlist)):
    if x == randomlist[i]:
        count += 1
        countloopstep +=1
        positionlist.append(i+1)
    else:
        countloopstep += 1
if count == 0:
    print("Not found")
else:
    print("The position list: ",positionlist)
    print("The number of loop step to find this number: ",countloopstep)
    