def partition(arr,low,high):
    p=arr[low]
    i=low+1
    j=high
    while True:
        while i<=j and arr[i]<=p:
            i +=1
        while i<=j and arr[j]>=p:
            j -=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j
def quick_short(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quick_short(arr,low,pivot-1)
        quick_short(arr,pivot+1,high)
arr=[4,9,5,7]
n=len(arr)
quick_short(arr,0,n-1)
print(arr)