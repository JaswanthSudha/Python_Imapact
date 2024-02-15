list=[]
def function(arr):
    new_arr=arr.copy()
    for i in range(len(arr)):
        max=arr[i]
        index_j=-1
        for j in range(i+1,len(arr)):
            if arr[j]>=max:
                max=arr[j]
                index_j=j
                element=arr[index_j]
        if index_j!=-1:
            # print(new_arr[i])
            # print(new_arr.index(element))
            print(new_arr.index(new_arr[index_j]))
            arr[i],arr[index_j]=arr[index_j],arr[i]
            # print(new_arr.index(new_arr[index_j]))
            
            
    print(arr)
    # print(new_arr)
function(list)

            

# print(list)
        



