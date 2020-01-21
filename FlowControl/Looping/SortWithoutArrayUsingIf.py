first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

small = 0
middle = 0
large = 0

if (first <= third and first <= second):
    small = first
    if(third<=second):
        middle=third
        large=second
    else:
        middle=second
        large=third

elif (second <=third and second <= first):
    small = second
    if(first<=third):
        middle=first
    else:
        middle= third
        large=first
else:
    if(first<=second):
         small=third
         middle=first
         large=second
    else:
        small=third
        middle=second
        large=first


# Display Results
print("The numbers in ascending order are: ", small, middle, large)