def move_zeroes(array):
# array=list(map(int,input().split(",")))
    k=-1
    for i in range(len(array)):
        if array[i]!=0:
            array[k+1]=array[i]
            k+=1
    if k==-1:
        return array
    for j in range(k+1,len(array)):
        array[j]=0
    return array
array=list(map(int,input().split(",")))
ans=move_zeroes(array)
print(ans)
