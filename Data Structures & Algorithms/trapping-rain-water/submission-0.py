class Solution:
    def trap(self, h: List[int]) -> int:
        n=len(h)
        if n==0:
            return 0
        t=0
        sm=[0]*n
        pmx=h[0]
        sm[n-1]=h[n-1]
        for i in range(n-2,-1,-1):
            sm[i]=max(sm[i+1],h[i])
            
        for i in range(1,n-1):
            if h[i]<pmx and h[i]<sm[i]:
                t+=min(pmx,sm[i])-h[i]
            pmx=max(pmx,h[i])
        return t
        
        
        