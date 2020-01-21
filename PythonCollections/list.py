# to declare
mylist=[]
print (type(mylist))

# list elements can be of different
mylist1 = [1, 2, 3, 4, 5, 'Hello']
print(mylist1)

# Duplicate Entries are possible
mylist2 =[1,1,2,2]
print(mylist2)

#It is mutable
mylist3=[1,2,3,4]
mylist3[1]='surya'
print(mylist3)

#insertion order is preserved

#to append at the end of list
mylist3.append(10000)
print(mylist3)

#to a particular postion
mylist3.insert(0,10000)
print(mylist3)

#iteration
#using index
mylist4=[1,2,3,3,5]
print(mylist4[0])
#not good practice if list is large

#for loop
cnt= len(mylist4)
for i in range(0,cnt):
    print(mylist4[i])