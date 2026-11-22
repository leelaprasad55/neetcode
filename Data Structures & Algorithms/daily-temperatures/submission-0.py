class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        r=[0]*len(temp)
        st=[]
        for i,k in enumerate(temp):
            while st and k>temp[st[-1]]:
                d=st.pop()
                r[d]=i-d
            
            
            st.append(i)
        return r