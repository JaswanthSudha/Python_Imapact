class Solution:
    def subArraySum(self,arr,s,n):
        sum=arr[0]
        start=0
        i=1
        while start<n:
            if sum>s:
                sum=sum-arr[start]
                start=start+1
            if sum==s:
                return [start+1,i]
            else:
                sum=sum+arr[i]
                i=i+1
        return -1
class DP:
    def subArraySum(self,arr,s,n):
        start=0
        end=-1
        sum=0
        hashmap={}
        for i in range(len(arr)):
            sum=sum+arr[i]
            if sum-s==0:
                start=1
                end=i+1
                return [start,end]
            if hashmap.get(sum-s):
                start=hashmap.get(sum-s)
                end=i
                return [start,end]
            hashmap[sum]=i
        return -1
            



            
# obj=Solution()
arr=[1]
n=1
s=0
obj=DP()
print(obj.subArraySum(arr,s,n))
        