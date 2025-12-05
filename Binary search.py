#Binary search
array=[9, 7, 5, 4, 6]
def Binary(arr,terget):
  left,right=0,len(arr)-1
  while left<=right:
    mid=(left+right)//2
    if arr[mid]==terget:
      return mid
    elif arr[mid]<terget:
      left=mid+1
    else:
      right=mid-1
  return -1
ss=Binary(array,7)
print(ss)