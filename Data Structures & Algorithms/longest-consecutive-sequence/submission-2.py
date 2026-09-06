class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            nums.sort()
            res=list(sorted(set(nums)))
            count=0
            maxcount=0
            for j in range(1,len(res)):
                if abs(res[j]-res[j-1])==1:
                    count+=1
                    maxcount=max(maxcount,count)
                else:
                    count=0
            return maxcount+1
        return 0