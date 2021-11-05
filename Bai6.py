import random

def sinh_ngau_nhien_danh_sach_so_nguyen():
    n = int(input("Enter the number of list: "))
    max_value = int(input("Enter the greatest number: "))
    a = [random.randrange(0,max_value) for i in range(n)]
    print("Random list:",a)
    return a
    
def sap_xep_tang_dan(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if (a[i] > a[j]):
                a[i],a[j] = a[j],a[i]
    return a

def sap_xep_giam_dan(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if (a[i] < a[j]):
                a[i],a[j] = a[j],a[i]
    return a

def check_option_user(a):
    check = input("Sort ascending order(Press 1) or descending order(Press 2): ")
    while (check != "1") and (check != "2"):
        print("Input error. Please try again")
        check = input("Sort ascending order(Press 1) or descending order(Press 2): ")
    if (check == "1"):
        sap_xep_tang_dan(a)
    else:
        sap_xep_giam_dan(a)
    return a

def main():
    a = sinh_ngau_nhien_danh_sach_so_nguyen()
    a = check_option_user(a)
    print(a)

if __name__ == "__main__":
    main()
