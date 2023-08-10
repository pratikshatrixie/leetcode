nums = [-1,2,1,-4]
s=float('inf')
target = 1
flag = 0
t=len(nums)
nums.sort()
for x in range(t-2):
    i=x+1
    j=t-1
    while i<j:
        s1=nums[x]+nums[i]+nums[j]
        if s1==target:
            break
            flag = 1
        if abs(target-s)>abs(target-s1):
            s=s1
        if s1<target:
            i+=1
        else:
            j-=1
    if flag == 1:
        break

if flag == 1:
    print(target)
else:
    print(s)