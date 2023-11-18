gpa=0
count=0
while True:
    n=input("Nhap diem (bang chu):")
    if n=="":
        break
    if n in ("A+","A"):
        x=4
    elif n=="B":
        x=3.5
    gpa=gpa+x
    count=count+1
print(round(gpa/count,1))