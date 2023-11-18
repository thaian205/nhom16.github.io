x=int(input("Nhap gia tri bat ki: "))
count=0
sum=0.0
if x==0:
    print("Ket thuc chuong trinh")
    exit()
while x!=0:
    sum += x
    count += 1
    x=int(input("Nhap gia tri bat ki( Nhap 0 de ket thuc): "))
print ("Trung binh cong:", (sum/count))