class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        ab=['+','-','*','/']
        for i in tokens:
            if i not in ab:
                s.append(int(i))
            else:
                a=s.pop()
                b=s.pop()
                if i=='+':
                    s.append(a+b)
                elif i=='-':
                    s.append(b-a)
                elif i=='*':
                    s.append(a*b)
                else:
                    s.append(int(b/a))
        return s[-1]

        