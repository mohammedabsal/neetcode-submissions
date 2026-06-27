class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            c="".join(sorted(s))
            if c not in d:
                d[c]=[s]
            else:
                d[c].append(s)
        return list(d.values())