a = input("Nhập số nhị phân: ")
b = 0
for i in range(len(a)):
    b += int(a[i]) * 2**(len(a)-i-1)
print("Số thập phân tương ứng là:", b)
