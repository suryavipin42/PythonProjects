ls=[]
numbers= input("enter the numbers separated by space")
ls= [int(i) for i in numbers.split()]
ls.sort()
sum_search=int(input("enter the number"))
upper=len(ls)-1
lower=0
while(lower<=upper):



    if((ls[lower]+ls[upper])==sum_search):
        print("(", ls[lower],
              ", ", ls[upper],
              ")", sep="")

        lower=lower+1
       # upper=len(ls)-1

    elif((ls[lower]+ls[upper])>sum_search):
        upper=upper-1
    else:
        lower=lower+1
