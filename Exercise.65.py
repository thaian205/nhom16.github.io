import math
def khoang_cach(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x = input("Nhập phần x của tọa độ: ")
y = input("Nhập phần y của tọa độ: ")
x1, y1 = float(x), float(y)
x_1, y_1 = x1, y1
chuvi = 0

while True:
  x=input('Nhập phần x của tọa độ: (trống để thoát): ')
  if x == '' :
     break
  y = input("Nhập phần y của tọa độ: ")
  x2, y2 = float(x), float(y)
  chuvi += khoang_cach(x1, y1, x2, y2)
  x1, y1 = x2, y2

chuvi += khoang_cach(x1, y1, x_1, y_1)
print(f"Chu vi của đa giác đó là {chuvi}")