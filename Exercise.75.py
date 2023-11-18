n = int(input("Nhập số nguyên dương thứ nhất: "))
m = int(input("Nhập số nguyên dương thứ hai: "))
if n < m:
    d = n
else:
    d = m
while d > 0:
    if n % d == 0 and m % d == 0:
        break
    d = d-1
print("Ước chung lớn nhất của", n, "và", m, "là", d)