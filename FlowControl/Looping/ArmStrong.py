num=int(input("enter the num"))
sum=0
digit=0
while(num!=0):
    digit=num%10
    sum=sum+digit**3
    num=num//10
print(sum)

