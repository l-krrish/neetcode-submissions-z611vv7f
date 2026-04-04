class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_unique = []
        for i in nums:
            if i not in nums_unique:
                nums_unique.append(i)
        
        
        for i in range(len(nums_unique)):
            nums[i] = nums_unique[i]
        
        return len(nums_unique)