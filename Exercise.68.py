while True:
    count=0
    n=input("Nhap 8 bit: ")
    if n=="":
        break
    if len(n) != 8:
        print("Lỗi: Nhập chuỗi 8 bit")
        continue
    for i in range(0,8):
        if n[i]=="1":
            count+=1
    if count%2==0:
            print("0")
    else:
            print("1")