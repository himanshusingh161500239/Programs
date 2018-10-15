def f1():
    ch=input()
    if(ord(ch)>=65 and ord(ch)<=90):
        if(ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
            print("Vowel")
        else:
            print("Consonant")
    elif(ord(ch)>=97 and ord(ch)<=122):
        if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("invalid")
f1()