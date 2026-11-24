class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=sorted(zip(position,speed),reverse=True)
        f=0
        st=0
        for p,s in car:
            time=(target-p)/s
            if time>st:
                f+=1
                st=time
        return f
        