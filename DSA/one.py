def function(n):
    if n==0 or n==1:
        return n
    return function(n-1)+function(n-2)
print(function(9))