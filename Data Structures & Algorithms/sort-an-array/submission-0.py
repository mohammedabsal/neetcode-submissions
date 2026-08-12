class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        flag=True
        while flag:
            flag=False
            for i in range(1,len(nums)):
                if nums[i-1]>nums[i]:
                    flag=True
                    nums[i-1],nums[i]=nums[i],nums[i-1]
        return nums