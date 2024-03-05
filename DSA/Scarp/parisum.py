# def pairsum(arr,k):
#     sum=0
#     for i in range(len(arr)):
#         if k-arr[i] in arr[i+1:]:
#             count=arr[i+1:].count(k-arr[i])
#             sum=sum+count
#     return sum
# numbers_list = [48, 24, 99, 51, 33, 39, 29, 83, 74, 72, 22, 46, 40, 51, 67, 37, 78, 76, 26, 28, 76, 25, 10, 65, 64, 47, 34, 88, 26, 49, 86, 73, 73, 36, 75, 5, 26, 4, 39, 99, 27, 12, 97, 67, 63, 15, 3, 92, 90]
# print(pairsum(numbers_list,50))
A=list(map(int,input().split()))
D=int(input("Enter D"))
N=len(A)
temp_array=[]
for i in range(D,N):
    temp_array.append(A[i])
for j in range(0,D):
    temp_array.append(A[j])
for i in range(N):
    A[i]=temp_array[i]
# 29 42 51 94 1 35 65 25 40 13 27 87 95 40 96 71 35 79 68 2 98 3 18 93 53 57 2 81 87 42 66 90 45 20 41 30 32 18 98 72 82 76 10 28 68 57 98 54 87 66 7 84 20 25 29 72 33 30 4 20 71 69 9 16 41 50 97 24 19 46 47 52 22 56 80 89 65