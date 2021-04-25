from array import *
print("Enter  value of n: ")
arr = array('i',[])
n = int(input())
print("Enter array:")
for i in range(n):
    inp = int(input())
    arr.append(inp)
print("the array is: ")
print(arr)
print("Enter a number to search: ")
x = int(input())
count = 0
for i in arr:
    if i == x:
        print(f"Index: {x}")
        break;
    count+=1
