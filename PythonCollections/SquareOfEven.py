limit=int(input("limit"))
even,odd,even_sq=[],[],[]
sum=0
for i in range (0,limit):
    num=int(input('enter the numbers'))
    if(num%2==0):
        even.append(num)
        even_sq.append(num*num)
        sum = sum+(num*num)
    else:
        odd.append(num)
print("even:",even)
print("even_sq:",even_sq)
print("sum of squares:",sum)
print("odd:",odd)

