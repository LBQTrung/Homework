def nhap_danh_sach_so_thuc():
    a = []
    check = ""
    while (check != "N") and (check != "n"):
        n = float(input("Enter the number: "))
        a.append(n)
        check = input("Press 'N' or 'n' to finish, others to continue: ")
    return a

def sap_xep_danh_sach_so_thuc(x):
    for i in range(0,len(x)-1):
        for j in range(i+1,len(x)):
            if (x[i] < x[j]):
                x[i],x[j] = x[j],x[i]
    return x

def main():
    x = nhap_danh_sach_so_thuc()
    x = sap_xep_danh_sach_so_thuc(x)
    print("Sort list descending:",x)

if __name__ == "__main__":
    main()