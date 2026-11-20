class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        while i<len(s):
            if s[i].isdigit() or s[i].isalpha():
                i+=1
            else:
                s=s[:i]+s[i+1:]
        j=0
        k=len(s)-1
        while j<k:
            if s[j].lower()!=s[k].lower():
                return False
            j+=1
            k-=1
        return True