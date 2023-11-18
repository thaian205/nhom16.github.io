tonggia=0
while True:
    gia= float(input("Nhap gia hoang hoa( nhap 0 de ket thuc): "))
    if gia==0:
        break
    tonggia+=gia
tongxu=tonggia*100
sodu=tongxu%5
if sodu<2.5:
    tong=tongxu-sodu
else:
    tong=tongxu+(5-sodu)
sotien=tong/100
print("Tong thanh toan: $",tonggia)
print("So tien phai tra neu thanh toan bang tien mat: $", sotien)