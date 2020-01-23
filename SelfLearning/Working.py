#
#  numb_list = []
#  numbers = input("Enter three numbers separated by space: ")
#
# numb_list = [int(i) for i in numbers.split()]
# print(numb_list)
#
#

# stack=[]
# numbers = input("Enter numbers separated by space: ")
# stack = [int(i) for i in numbers.split()]
# print("intial",stack)
# print('\nElements poped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# stack.append('a')
# print(stack)
def printPairs(arr, n, sum):

  for i in range(0, n):
    for j in range(i + 1, n):
       if (arr[i] + arr[j] == sum):
          print("(", arr[i],
          ", ", arr[j],
          ")", sep="")


arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 8
printPairs(arr, n, sum)