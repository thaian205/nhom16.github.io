print(end= '    ')
for i in range(1,11):
  s = str(i)
  s = s.rjust(3)
  print(s,end=' ')
print()
for i in range(1,11):
  a = str(i)
  a = a.rjust(3)
  print(a,end=' ')
  for j in range(1,11):
    k = str(i*j)
    k = k.rjust(3)
    print(k,end=' ')
  print()