list=[4,21,1,9,2,67,45,3,0]
for i in range(1,len(list)):
    key=list[i]
    j=i-1
    while j>=0 and list[j]>key:
        list[j+1]=list[j]
        j=j-1
    list[j+1]=key
print(list)




    
    

        

    

    
