class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        for num in nums:
            d[num] = d.get(num,0)+1
        re=[i for i,v in d.items() if v>n//2]
        return re[0]


