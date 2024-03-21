if __name__=="__main__":
    s=input()
    x=int(s)
    max1=-1
    while x!=0:
        r=x%10
        if r%2!=0 and r>max1:
            max1=r
        x=x//10
    print(max1)




    