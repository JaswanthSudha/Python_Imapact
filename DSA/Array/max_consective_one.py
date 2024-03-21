array=list(map(int,input().split(",")))
max1=0
k=0
for i in range(len(array)):
    if array[i]==1:
        k+=1
    else:
        if k>max1:
            max1=k
            k=0
if k>max1:
    max1=k
print(max1)