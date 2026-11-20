class Solution:
    def maxArea(self, h: List[int]) -> int:
        mx=float('-inf')
        i,j=0,len(h)-1
        while i<j:
            dis=j-i
            m1=min(h[i],h[j])
            t=m1*dis
            mx=max(mx,t)
            if h[i]<h[j]:
                i+=1
            else:
                j-=1
        return mx