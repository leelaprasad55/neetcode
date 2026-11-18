class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        m=0
        for i in s:
            c=1
            if i-1 not in s:
                while i+c in s:
                    c+=1
            m=max(m,c)
        return m