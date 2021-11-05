def nhap_danh_sach_so_nguyen(n):
    a = [int(input("Nhập số nguyên: ")) for i in range(0,n)]
    return a

def sap_xep_danh_sach(x):
    for i in range(0,len(x)-1):
        for j in range(i+1,len(x)):
            if (x[i] > x[j]):
                x[i],x[j] = x[j],x[i]
    return x

def main():
    n = int(input("Nhập số phần từ của danh sách: "))
    x = nhap_danh_sach_so_nguyen(n)
    x = sap_xep_danh_sach(x)
    print("Danh sách tăng dần:",x)

if __name__ == "__main__":
    main()