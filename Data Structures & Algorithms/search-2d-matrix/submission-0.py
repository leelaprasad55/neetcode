class Solution:
    def searchMatrix(self, ma: List[List[int]], t: int) -> bool:
        i,j=0,len(ma)-1
        while i<=j:
            m=(i+j)//2
            k,l=0,len(ma[0])-1
            if ma[m][l]>=t>=ma[m][k]:
                while k<=l:
                    m1=(k+l)//2
                    if ma[m][m1]==t:
                        return True
                    elif ma[m][m1]>t:
                        l=m1-1
                    else:
                        k=m1+1
                return False
            elif t>ma[m][l]:
                i=m+1
            elif t<ma[m][k]:
                j=m-1
        return False