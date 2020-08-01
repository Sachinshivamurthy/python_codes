arr=[9,30,4,8,23]
n=len(arr)
for i in range(n):
    min=i
    for j in range(i+1,n):
        if (arr[j]<arr[min]):
            min=j
    arr[i],arr[min]=arr[min],arr[i]
print("sort",arr)
