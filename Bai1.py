a = [int(input("Enter the number: ")) for i in range(0,10)] #Input 10 integer numbers

# Sort ascending
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if (a[i] > a[j]):
            a[i],a[j] = a[j],a[i]

print("List of numbers after sorting: ",a)
