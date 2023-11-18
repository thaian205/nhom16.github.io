soluong_treem= 0
soluong_caotuoi= 0
soluong_ngkhac= 0
gia=0
while True:
    age=input("Nhap so tuoi(de trong de ket thuc): ")
    if age=="":
        break
    else:
        age_int=int(age)
        if age_int<=2:
            continue
        elif age_int<=12:
            soluong_treem +=1
            gia=gia+14.00
        elif age_int<=65:
            soluong_ngkhac += 1
            gia=gia+18.00
        else:
            soluong_caotuoi += 1
            gia=gia+23.00
print("Tong so luong tre em:",soluong_treem)
print("Tong so luong người cao tuoi:",soluong_caotuoi)
print("Tong so luong khach khac:",soluong_ngkhac)
print("Tong chi phi: $",gia)
