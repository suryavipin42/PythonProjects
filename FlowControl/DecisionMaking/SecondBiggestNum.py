num1= float(input("enter the num"))
num2= float(input("enter the num"))
num3= float(input("enter the num"))
if(num1>num2)&(num1<num3):
    print(num1,"is second largest")
elif(num2>num1)&(num2<num3):
    print(num2,"is the second largest")
else:
    print(num3, "is the second largest")
#else:
 #   if(num2>num3):
  #  print(num3,"is the second largest")
