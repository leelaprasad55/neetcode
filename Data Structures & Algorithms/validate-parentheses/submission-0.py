class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={'{':'}','[':']','(':')'}
        for i in s:
            if i in d:
                st.append(i)
            else:
                if not st or i!=d[st.pop()]:
                    return False
        return len(st)==0 
