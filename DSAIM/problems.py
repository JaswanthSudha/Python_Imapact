# from sum_digit import sum_digit
# # # array=list(map(int,input().split()))
# # # def max(array):
# # # 	max1=array[0]
# # # 	for item in array:
# # # 		if max1<item:
# # # 			max1=item
# # # 	print(max1)
# # # def duplicated(array):
# # # 	n=len(array)*2
# # # 	b=[0]*n
# # # 	for i in range(len(array)):
# # # 		b[i]=array[i]
# # # 		b[i+len(array)]=array[i]
# # # 	print(b)
# # # def unique(array):
# # # 	for i in range(len(array)):
# # # 		if array[i] not in array[i+1:]:
# # # 			print(array[i],end=" ")
# # # # duplicated(array)
# # # unique(array)
# # a,b,c=map(int,input().split())
# # list=[a,b,c]
# # sum1=sum(list)
# # count=0
# # for item in list:
# #     if sum1-item>item:
# #         count=count+1
# # if count==3:
# #     print("yes")
# # else:
# #     print("no")
# # def power(a,b):
# #     if b==0:
# #         return 1
# #     return a*power(a,b-1)
# # a,b=map(int,input().split())
# # print(power(a,b))
# # list1=list(map(int,input().split()))
# # sum1=sum(list1)
# # sum2=sum([i for i in range(1,101)])
# # print(sum2-sum1)
# # def factorial(n):
# #     if n==1:
# #         return 1
# #     return n*factorial(n-1)

# # print(factorial(5))

# def fibonaci(a):
#     if a in [0,1]:
#         return a
#     return fibonaci(a-1)+fibonaci(a-2)
# # a=int(input("enter a"))
# # print(fibonaci(a))
# def test_pytest():
#     assert fibonaci(3)==2
# n=100
# sum=0
# for i in range(1,n+1):
#     if i%3==0 or i%5 ==0:
#           sum=sum+1
# print(sum)
# def number(a):
#     return a//3+a//5-a//15
# # print(12//15//-7//15)
# print(12//3)
# def length(a):
#     x=str(a)
#     return len(x)
# n=int(input("enter a number"))
# p=length(n)
# x=n
# sum=0
# while n!=0:
#     r=int(n%10)
#     sum=sum+(r**p)
#     n=n//10
# if sum==x:
#     print("yes")
# else:
#     print("no")
# n=int(input("enter"))
# reverse=0
# while n!=0:
#     r=n%10
#     reverse=(reverse*10)+r
#     n=n//10
# print(reverse)
# count=0
# n=6
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(count,end=" ")
#         count=count+1
# op="*"
# for i in range(1,n):
#     # op=op*i
#     print(op*i)
# for i in range(1,n+1):
#     x=i
#     l=n-1
#     for j in range(1,i+1):
#         print(x,end=" ")
#         x=x+l
#         l=l-1   
#     print()
# l=int(input("enter length"))
# h=int(input("enter height"))
# print("*"*l)
# for i in range(1,h+1):
#     print("*",end="")
#     for y in range(l-2):
#         print(" ",end="")
#     print("*",end="")
#     print("")
# print("*"*l)
# n=int(input("enter n"))
# for i in range(1,n+1):
#     print("*"*i,end="")
#     print("")
# for i in range(n,0,-1):
#     print("*"*(i),end="")
#     print("")
# for i in range(n):
#     print(" "*(n-i),end="")
#     print("* "*(i),end="")
#     print()
# string=input("enter")
# print(list(string).count("ch"))
# item=input("enter the character")

# count=0
# for ch in string:
#     if ch==item:
#         count=count+1
# print(count)
# for i in range(n,0,-1):
#     print()
# string=input("enter string ")
# list1=string.split()
# word=input("enter the character ")
# count=0
# for item in list1:
#     if item==word:
#         count=count+1
# print(count)
# flag=0
# for item in list1:
#     if item in ['a','e','i','o','u']:
#         print("yes")
#         flag=1
#         break
# if flag==1:
#     print("yes")
# else:
#     print("no")
# flag=False
# for item in list1:
#     for ch in item:
#         if ch in ['a','e','i','o','u']:
            
# if flag:
#     print("No")
# else:
#     print("Yes")
# print("A".lower())
# print("124".isnumeric()) 
# str=input("enter the string")
# newString=""
# # print(str.swapcase())
# for ch in str:
#     if ch ==ch.lower():
#         newString=newString+ch.upper()
#     else:
#         newString=newString+ch.lower()
# print(newString)
# n=int(input("enter"))
# string="G"+"o"*n+"d"
# print(string)
# print("G"+"o"*int(input())+"d")
# print("".join(set(input())))
# string=input("enter")
# list1=list(string)
# set2=set(list1)
# newString=""
# for item in set2:
#     newString=newString+item
#     newString=newString+str(list1.count(item))
# print(newString)
# map={}
# for item in string:
#     if item not in map:
#         map[item]=1
#     else:
#        value= map.get(item)
#        map[item]=value+1
# string2=""
# for item in map:
#     string2=string2+item+str(map.get(item))
# print(string2)







        



   


