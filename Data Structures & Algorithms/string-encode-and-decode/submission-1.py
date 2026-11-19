class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s=s+'—'+i
        return s 

    def decode(self, s: str) -> List[str]:
        l=list(map(str,s.split('—')))
        return l[1:]