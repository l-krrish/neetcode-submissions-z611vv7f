class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            c=nums.count(nums[i])
            if c>1:
                return True
        return False