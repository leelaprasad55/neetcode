class Solution:
    def maxProfit(self, p: List[int]) -> int:
        lm=p[-1]
        mx=0
        for i in range(len(p)-2,-1,-1):
            diff=lm-p[i]
            mx=max(mx,diff)
            lm=max(lm,p[i])
        return mx