class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r=set()
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            s=set()
            for j in range(i+1,len(nums)):
                k=-(nums[i]+nums[j])
                if k in s:
                    r.add((nums[i],nums[j],k))
                s.add(nums[j])
        return [list(re) for re in r] 