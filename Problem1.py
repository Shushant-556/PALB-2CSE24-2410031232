class Solution:
    def reverseArray(self,arr):
        left,right=0,len(arr)-1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
arr=list(map(int,input("Enter arr:").split()))
Solution().reverseArray(arr)
print("ReversedArrray:",arr)