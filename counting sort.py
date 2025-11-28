def counting(arr):
    if not arr:
        return arr
    
    max_val=max(arr)
    count=[0]*(max_val+1)

    for num in arr:
        count[num]+=1
    arr[:]=[]

    for num,frcq in enumerate(count):
        arr.extend([num]*frcq)

    return arr
unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = counting(unsortedArr)
print("Sorted array:", sortedArr)