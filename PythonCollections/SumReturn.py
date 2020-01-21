limit=int(input("limit"))
numlist =[]
for i in range(0,limit):
    num=int(input("enter the numbers"))
    numlist.append(num)
element=int
for i in range(0,limit):
    if(numlist[i]+numlist[i+1]==element):
