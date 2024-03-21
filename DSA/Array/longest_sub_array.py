a=list(map(int,input().split(",")))
ans=[]
k=10
sum1=0
for i in range(len(a)):
    for j in range(i,len(a)):
        sum1+=a[j]
        if sum1==k:
            ans.append(j-i+1)
        if sum1>k:
            break
    sum1=0
print(max(ans))




    
    




