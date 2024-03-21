def binarySearch(array,left,right,target):
    while left<right:
        mid=(right+left)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return -1
array=[3, 4, 6, 7, 9, 12, 16, 17]
target=60
output=binarySearch(array,0,len(array)-1,target)
print(output)


