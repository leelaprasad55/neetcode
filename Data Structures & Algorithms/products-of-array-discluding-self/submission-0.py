class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        p,s=1,1
        l=[1]*n
        for i in range(n):
            l[i]=p
            p*=nums[i]
        for j in range(n-1,-1,-1):
            l[j]*=s
            s*=nums[j]
        return l
        