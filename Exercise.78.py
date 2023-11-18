q = int(input("Nhập số thập phân: "))
result = ""
while q > 0:
    r = q % 2
    result = str(r) + result
    q = q // 2
print("Số nhị phân tương ứng là:", result)
