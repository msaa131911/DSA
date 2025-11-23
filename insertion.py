#insertion
arr=[40,30,20,10]
n=len(arr) #n=4
for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j -=1
    arr[j+1]=key

print(arr)
