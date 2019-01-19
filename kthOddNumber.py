n,k=map(int,input().split())
arr=list(map(int,input().split()))
count=0
for i in range(0,len(arr)):
    if(arr[i]%2!=0):
        count+=1
    if(count==k):
        print(arr[i])
        break
