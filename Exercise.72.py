b = input("Nhập chuỗi: ")
a=""
for i in range(len(b)- 1, -1, -1):
    a += b[i]
if b == a:
    print("Chuỗi là palindrome")
else:
    print("Chuỗi không phải là palindrome")