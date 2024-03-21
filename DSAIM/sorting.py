# #BubbleSort
# array=list(map(int,input().split()))
# swap=0
# for i in range(len(array)):
#     # x=0
#     for j in range(len(array)):
#         if array[i]>array[j]:
#             array[i],array[j]=array[j],array[1]
#             swap+=1
# print(swap)
#QuickSort
# algorithm(Quick_Sort(list))
# Pre:list 6=fi
# POst:the list has been sorted in ascending order
# if list.Count =1 //list already sorted
# return list
# end if 
# pivot <-Median_value(list)
# for i<-0 
# if List[i]<pivot
# Less .insert(list)
# end if 
# fi list[i]>pivot
# Greater .insert(list(i))
# end if
# end for
# def Partion(array):
#     return array[0]
# def swap(a,b):
#     a,b=b,a
# def QuickSort(array):
#     left_index=0
#     right_index=len(array)-1
#     pi=Partion(array)
#     for i in range(len(array)):
#         if array[left_index]>array[right_index]:
#             swap(array[left_index,right_index])
#     QuickSort(array[0])
#     QuickSort(array[1])
#     print(array)
#merge Sort
# def merge(array,left,mid,right):
#     array1=array[left:mid]
#     array2=array[mid+1:right]
#     n1=len(array1)
#     n2=len(array2)
#     i,j=0
#     k=0
#     while i<n1 and j<n2:
#         if array1[i]<array2[j]:
#             array[k]=array[i]
#             i+=1
#             k+=1
#         else:
#             array[k]=array[j]
#             j+=1
#             k+=1
#     while i<=n1:
#         array[k]=array[i]
#         i+=1
#         k+=1
#     while j<=n2:
#         array[k]=array[j]
#         j+=1
#         k+=1
# def mergesort(array,left,right):
#     if left<right:
#         mid=(left+right)//2
#         mergesort(array,left,mid)
#         mergesort(array,mid+1,right)
#         merge(array,left,mid,right)
# mergesort(array,0,len(array)-1)
# print(array)
#selection_sort
# index_j=-1
# for i in range(len(array)):
#     max=array[i]
#     index_j=-1
#     for j in range(i,len(array)):
#         if max>array[j]:
#             max=array[j]
#             index_j=j
#         if index_j!=-1:
#             array[i],array[index_j]=array[index_j],array[i]
# print(array)
#insertion_sort
# sorted_index=0
# for i in range(1,len(array)):
#     for j in range(0,sorted_index):
#         if array[i]<array[j]:
#             array[j],array[i]=array[i],array[j]
#             sorted_index+=1
# print(array)
    
    
