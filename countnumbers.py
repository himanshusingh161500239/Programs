def f():
    n=int(input())
    count=0
    if(n>0):
        while(n>0):
            n=n//10
            count=count+1
    elif(n==0):
        count=1
    elif(n<0):
        n=-(n)
        while(n>0):
            n=n//10
            count=count+1
    print(count)
f()