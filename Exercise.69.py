s=3
i=1
n=2
while i<=15:
    p=4*(1/((n*(n+1)*(n+2))))
    n=n+2
    q=-4*(1/((n)*(n+1)*(n+2)))
    n=n+2
    s+=p+q
    print("pi=",s)
    i+=1