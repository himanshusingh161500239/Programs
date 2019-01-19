n,k=map(int,input().split())
count=0
temp1=k
while(k>0):
    count=count+1
    k=k//10  
temp=1
while(count>0):
    temp=temp*10
    count=count-1
n=n*temp
n=n+temp1
print(n)
    
