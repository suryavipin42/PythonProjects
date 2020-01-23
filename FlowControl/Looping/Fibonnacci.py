lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
A=0
B=0
C=0
while(C<=upper):
    if(C>lower):
        print(A)
        C = A + B
        A = B
        B = C

