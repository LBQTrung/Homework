import random
n = int(input("The number of list: "))
print("Enter the range [a,b] to random")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

randomlist = [random.randrange(a,b+1) for i in range(0,n)]
print("random list: ",randomlist)

inputstring = "Enter the number need to find (" + str(a) +" =< x <= "+ str(b) +"): "
x = int(input(inputstring))
while (x < a) or (x > b):
    print("Input error. Please try again")
    x = int(input(inputstring))

countstep = 0
for i in range(0,n):
    if x == randomlist[i]:
        print("The first position in random list: ",i+1)
        countstep += 1
        break
    else:
        countstep += 1
if (countstep == n):
    print("Not found")
else:
    print("The number of step to find this number: ",countstep)