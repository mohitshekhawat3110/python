n= [13,7,6,5]
c= 0
for i in n:
    f=0
    for j in range (2,i):
        if (i%j ==0):
            f=1
            break;
        if(f==0):
            c=c+1
if (len(n)==c):
    print("correct")
else:
     s=0
     for j in range (2,s):
            if(s%j==0:
         print ("inCorrect")
            f=0
            break;
        if(f==1):
            print("correct")
