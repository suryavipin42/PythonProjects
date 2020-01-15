mark1=float(input("enter the mark of Eng"))
mark2=float(input("enter the mark of Maths"))
mark3=float(input("enter the mark of Science"))
total= mark1+mark2+mark3
if (total>145):
    print("A+")
elif(total>=140):#&(total<=145):
    print("A")
elif(total>=135):#&(total<=140):
    print("B+")
elif(total>=130):#&(total<=135):
    print("B")
else:
    print("failed")