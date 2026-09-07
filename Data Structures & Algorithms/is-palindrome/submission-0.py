import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        es=re.findall(r'[A-Za-z0-9]+',s.lower())
        res="".join(es)
        l=0
        r=len(res)-1
        while l<r:
            if res[l]!=res[r]:
                return False
            l+=1
            r-=1
        return True