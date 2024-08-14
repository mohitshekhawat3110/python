
#palindrom
n = int(input("enter a number:"))
s=0
while (n!=0):
    r=n%10
    s=s*10+r
    n=n//10
    print("reverse value is =  ",s)
if (t ==s):
    print ("no is pal")
else:
    print ("no is not pal")
