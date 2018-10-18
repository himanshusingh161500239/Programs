def f():
    m,n=map(int,input().split())
    if(m>0 and n>=0):
        power=m**n
    elif(m==0):
        power=0
    elif(m<0 and n>=0 and n%2==0):
        m=-(m)
        power=m**n
    elif(m<0 and n>=0 and n%2!=0):
        power=m**n
    print(power)
f()