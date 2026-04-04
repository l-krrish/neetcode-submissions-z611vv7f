class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_unique=[]
        for i in range(len(nums)):
            if nums[i] not in nums_unique:
                nums_unique.append(nums[i])
        nums[:]=nums_unique
        return len(nums)