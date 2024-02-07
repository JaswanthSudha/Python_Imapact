list=[4,21,1,9,2,67,45,3,0]
index=0
index_j=-1
for i in range(len(list)):
    min_value=list[i]
    for j in range(index,len(list)):
        if min_value>list[j]:
            min_value=list[j]
            index_j=j
    if index_j!=-1:
        list[i],list[index_j]=list[index_j],list[i]
    index+=1
    index_j=-1
print(list)
        



