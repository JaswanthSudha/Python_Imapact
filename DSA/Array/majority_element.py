if __name__=="__main__":
    arr=list(map(int,input().split()))
    value=len(arr)//2
    maxi=-1
    hashmap={}
    for item in arr:
        hashmap[item]=hashmap.get(item,0)+1
    for item in arr:
        if hashmap[item]>=value:
            maxi=item
    print(maxi)


        
