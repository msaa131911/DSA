#Linear search
def linear(array,target):
  for i in range(len(array)):
    if array[i]==target:
      return i
  return -1
arr=[10,20,30,40]
n=int(input("enter your target:"))
ss=linear(arr,n)
print(ss)