from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=[[] for _ in range(len(nums) + 1)]
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for ke,v in d.items():
            c[v].append(ke)
        l = []
        for i in range(len(c) - 1, 0, -1):
            for num in c[i]:
                l.append(num)
                if len(l) == k:
                    return l    