nums=list(map(int,input().split()))
target=int(input())
d={}
for i in range(len(nums)):
    rem=target-nums[i]
    if rem in d:
        print([d[rem],i])
        break
    d[nums[i]]=i
