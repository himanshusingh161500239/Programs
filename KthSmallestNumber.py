n,k=map(int,input().split())
arr=list(map(int,input().split()))
while(k>0):
    smallest=arr[0]
    for i in arr:
        if(i<=smallest):
            smallest=i
    arr.remove(smallest)
    k=k-1
print(smallest)

        
