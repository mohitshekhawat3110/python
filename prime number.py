#prime number
n = int (input ("enter n="))
f=1
for i in range (2,n):
    if (n%i==0):
        f=0
        break
if(f==1):
        print("prime")
else:
        print("not prime")
