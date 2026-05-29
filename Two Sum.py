nums=[1,4,6,7,3]
target=10
n=len(nums)
for i in range(n-1): 
    for j in range(i+1,n):
        sum = nums[i]+nums[j]
    if sum == target: 
        print(i,j)
