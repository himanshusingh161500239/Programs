def f1():
    n,k=map(int,input().split())
    l = list(map(int, input().split()))
    sum=0
    for i in range(0,k):
        sum=sum+l[i]
    print(sum)
f1()