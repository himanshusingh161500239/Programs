def f1():
    year=int(input())
    if(year%400==0):
        print("yes")
    if(year%100==0):
        print("no")
    if(year%4==0):
        print("yes")
    else:
        print("no")
        
f1()
    