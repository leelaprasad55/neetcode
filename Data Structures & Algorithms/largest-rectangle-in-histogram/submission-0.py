class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        st=[]
        mx=0
        for i,v in enumerate(h+[0]):
            while st and h[st[-1]]>v:
                hi=h[st.pop()]
                w=i if not st else i-st[-1]-1
                c=hi*w
                mx=max(mx,c)

            



            st.append(i)
        return mx 