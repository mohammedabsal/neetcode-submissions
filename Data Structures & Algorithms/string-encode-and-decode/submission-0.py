class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for c in strs:
            s+=str(len(c))
            s+="#"
            s+=c
        return s
    def decode(self, s: str) -> List[str]:
        res=[]
        ## ex : 3#moh5#absal
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            num=int(s[i:j])
            j+=1
            word=s[j:j+num]
            res.append(word)
            i=j+num
        return res