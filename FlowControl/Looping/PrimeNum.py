num= int(input("enter the num"))
for i in range(2,num):
    if(num%i==0):
       flag=0
       break
    else:
        flag=1

if(flag==1):
    print("a prime num")
else:
    print("not prime")