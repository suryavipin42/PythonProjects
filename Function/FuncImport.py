# import Function.MathsOperations as a
num1=int(input("enter num1"))
num2=int(input("enter the num2"))
#
# add = a.add(num1,num2)
# print("add:{}".format(add))
#
# sub = a.subtract(num1,num2)
# print(sub)



# we can also use Function.MathsOperations instead of naming it as a.
#  For convenience you can use alias name
# path explicit( full path should be given to remove this use from)

# add * to import all

    # from Function.MathsOperations import *
    # add= add(num1,num2)
    # print(add)

from Function.MathsOperations import add
add= add(num1,num2)
print(add)
