stk=[]
top=0

size=int(input("enter the size of stack"))
while(top<=size):
    op=int(input("select operation 1.push 2.pop 3.display"))
    if(op==1):
        item =int(input("Enter the number to be stored"))
        push(item)
def push(item):
    stk.insert(top,item)
    top=top+1