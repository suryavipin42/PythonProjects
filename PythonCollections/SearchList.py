limit=int(input("limit"))
search=int(input("enter the number to be searched"))
flag=0
for i in range (0,limit):
    num=int(input("enter the numbers"))
    if(num==search):
        flag+=1
        break
    else:
        flag=0
if(flag==0):
    print("not found")
else:
    print("element found {} times".format(flag))


