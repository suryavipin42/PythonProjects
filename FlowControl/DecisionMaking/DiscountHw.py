print("enter the no. of material")
mat= int(input("1.cotton 2.silk 3.linen"))
amnt= float(input("enter the purchase amount"))
if(input==1):
    if(amnt>20000):
        DiscAmnt=amnt*(90/100)
        Discount=amnt-DiscAmnt
    elif(amnt>=15000):
        DiscAmnt=amnt*(91/100)
        Discount = amnt - DiscAmnt
    elif(amnt>=14000):
        DiscAmnt=amnt*(93/100)
        Discount = amnt - DiscAmnt
    else:
        DiscAmnt=amnt*(98/100)
        Discount = amnt - DiscAmnt
elif(input==2):
    if (amnt > 20000):
        DiscAmnt = amnt * (85 / 100)
        Discount = amnt - DiscAmnt
    elif (amnt >= 15000):
        DiscAmnt = amnt * (90/ 100)
        Discount = amnt - DiscAmnt
    elif (amnt >= 14000):
        DiscAmnt = amnt * (91 / 100)
        Discount = amnt - DiscAmnt
    else:
        DiscAmnt = amnt * (95 / 100)
        Discount = amnt - DiscAmnt
else:
    if (amnt > 20000):
        DiscAmnt = amnt * (85 / 100)
        Discount = amnt - DiscAmnt
    elif (amnt >= 15000):
        DiscAmnt = amnt * (90/ 100)
        Discount = amnt - DiscAmnt
    elif (amnt >= 14000):
        DiscAmnt = amnt * (91 / 100)
        Discount = amnt - DiscAmnt
    else:
        DiscAmnt = amnt * (95 / 100)
        Discount = amnt - DiscAmnt

print("Discount is :{} and amount to be paid is :{}".format(Discount,DiscAmnt))