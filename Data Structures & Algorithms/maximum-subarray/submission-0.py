class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=nums[0]
        window=nums[0]
        for num in nums[1:]:
            current=max(num,current+num)
            window=max(window,current)
        return window