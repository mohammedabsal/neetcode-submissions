class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        val=min(strs)
        res=""
        for i in range(len(val)):
            for s in strs:
                if s[i]!=val[i]:
                    return res
            res+=s[i]
        return res