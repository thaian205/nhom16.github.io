n = input('Nhap chuoi can ma hoa: ')
str =' '
for i in n:
  a = ord(i)
  if (a >=65 and a<= 87) or (a>=97 and a<=119):
    k = a
    k += 3
    str += chr(k)
  elif a == 88 or a==89 or a==90 or a==120 or a==121 or a==122:
    k = a
    k -= 23
    str += chr(k)
print(str)