a=[16,17,4,3,5,2]
ans=[]
sorted_array=sorted(a)
for i in range(len(a)-1):
    sub_array=a[i+1:len(a)]
    max_item=max(sub_array)
    if a[i]>max_item:
        ans.append(a[i])
custom_set=set()
custom_set.add(1)
custom_set.add(3)
custom_set.remove(1)
print(custom_set)
        

