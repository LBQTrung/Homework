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


if x in randomlist:
    print("The first position in this list: ",randomlist.index(x)+1)
else:
    print("Not found")
