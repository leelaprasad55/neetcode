class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            c=[0]*26
            for j in i:
                c[ord(j)-ord('a')]+=1
            t=tuple(c)
            if t not in d:
                d[t]=[]
            d[t].append(i)
        return list(d.values())
        
        