def merge(array,start,mid,end):
    n1=mid-start+1
    n2=end-mid
    list1=[0]*n1
    list2=[0]*n2
    for i in range(n1):
        list1[i]=array[start+i]
    for j in range(n2):
        list2[j]=array[end+start+j]
    i,j,k=0,0,start
    while i<n1 and j<n2:
        if list1[i]<list2[j]:
            array[k]=list1[i]
            i=i+1
            k=k+1
        if list1[i]>list2[j]:
            array[k]=list2[j]
            j=j+1
            k+=1
    while i<n1:
        array[k]=list1[i]
        i=i+1
        k=k+1
    while j<n2:
        array[k]=list2[j]
        j=j+1
        k+=1


    
def mergeSort(array,start,end):
    if start<end:
        mid=(start+end)//2
        mergeSort(array,start,mid)
        mergeSort(array,mid+1,end)
        merge(array,start,mid,end)
list=[4,21,1,9,2,67,45,3,0]
mergeSort(list,0,len(list)-1)
print(list)
