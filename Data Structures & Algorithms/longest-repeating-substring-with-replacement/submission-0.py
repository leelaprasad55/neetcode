class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        f={}
        mf=0
        a=0
        for r in range(len(s)):
            f[s[r]]=f.get(s[r],0)+1
            mf=max(mf,f[s[r]])
            if (r-l+1)-mf>k:
                f[s[l]]-=1
                l+=1
            a=max(a,r-l+1)
        return a