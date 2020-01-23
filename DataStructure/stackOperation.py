stk=[]
size=int(input("enter size"))
n=1
def push(item):
    print("inside push")


def pop():
    print("item popped out")

def display():
    print("inside displaY")

while(n!=0):
    option=int(input("select option 1)push 2)pop 3)delete"))

    if(option==1):
        push(10)
    elif(option==2):
        pop()
    elif(option==3):
        display()


    n=int(input("do u want to continue  press 0 to exit"))