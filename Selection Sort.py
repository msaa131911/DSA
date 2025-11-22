my_array = [64, 34, 25, 5, 22]
n=len(my_array)
for i in range(n-1):
    mini=i
    for j in range(i+1,n):
        if my_array[j]<my_array[mini]:
            mini=j
    my_array[i],my_array[mini]=my_array[mini],my_array[i]
print(my_array)