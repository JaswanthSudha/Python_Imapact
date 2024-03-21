
def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		print(j+1,end=" ")
		arr[j + 1] = key
arr = list(map(int,input().split()))
# insertionSort(arr)
# print(arr)
pointer0=0
pointer1=0
for i in range(len(arr)):
	if arr[i]==0:
		pointer0+=1
	else:
		pointer1+=1
list2=[0]*pointer0
list3=[1]*pointer1
list2.extend(*list3)


