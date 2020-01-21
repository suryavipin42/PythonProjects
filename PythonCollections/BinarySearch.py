limit=int(input("limit"))
numlist =[]
element=int(input("element to be searched"))
flag=0

for i in range(0,limit):
    num=int(input("enter the numbers"))
    numlist.append(num)
numlist.sort()
lower=0
upper=len(numlist)
mid=((upper+lower))//2
cnt=numlist.count(element)

while(lower<=upper):
    if(element>numlist[mid]):
        lower=mid+1
    elif(element<numlist[mid]):
        upper=mid-1
    elif(element==numlist[mid]):
        flag+=1
        break
    mid=(upper+lower)//2
if(flag!=0):
    print("element {} found {} times".format(element,cnt))
else:
    print("not found")