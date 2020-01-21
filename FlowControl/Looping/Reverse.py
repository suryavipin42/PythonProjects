num=int(input("enter the num"))
reverse=0
reminder=0
while(num>0):
    reminder= num%10
    reverse=reverse*10+reminder
    num=num//10
print(reverse)