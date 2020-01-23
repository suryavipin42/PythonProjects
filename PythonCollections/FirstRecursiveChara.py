
str=input("enter the string")
size=len(str)-1
for i in range(0,size):
  for j in range(1,size):
      if(str[i]==str[j]):
          print(str[i])
          break
      else:
          continue

