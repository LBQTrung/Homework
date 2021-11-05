a = []
check = ""

while (check != "N") and (check != "n"):
    n = float(input("Enter the number: "))
    a.append(n)
    check = input("Press 'N' or 'n' to finish, others to continue: ")

for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if (a[i] < a[j]):
            a[i],a[j] = a[j],a[i]
print(a)