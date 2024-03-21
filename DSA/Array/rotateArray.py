# array=list(map(int,input("Enter Array ").split()))
arr=[1,2,3,4,5,6,7]
k=3
temp=arr[:k].copy()
new_array=arr.copy()
for i in range(len(arr)-1,k-1,-1):
    arr[i-k]=new_array[i]
arr[-k:]=temp
print(arr)


