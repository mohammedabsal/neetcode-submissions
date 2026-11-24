class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for s in strs:
            ## checking the common one
            x="".join(sorted(s))
            d[x].append(s)
        return list(d.values())