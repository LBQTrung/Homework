import random

n = int(input("Enter the number of list: "))
max_value = int(input("Enter the greatest number: "))
a = [random.randrange(0,max_value) for i in range(n)]
print("Random list:",a)

'''Check option of user
    1: Sort list ascending order
    2: Sort list descending order
    others: Press again
'''
check = input("Sort ascending order(Press 1) or descending order(Press 2): ")
while (check != "1") and (check != "2"):
    print("Input error. Please try again")
    check = input("Sort ascending order(Press 1) or descending order(Press 2): ")

if check == "1":
    #Sort list ascending order
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if (a[i] > a[j]):
                a[i],a[j] = a[j],a[i]

else:
    #Sort list descending order
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if (a[i] < a[j]):
                a[i],a[j] = a[j],a[i]
                
print("List after sorting: ",a)