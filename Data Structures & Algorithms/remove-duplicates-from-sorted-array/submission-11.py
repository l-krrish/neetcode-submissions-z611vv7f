class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_unique=[]
        for num in nums:
            if num not in nums_unique:
                nums_unique.append(num)
        
        nums[:]=nums_unique

        return len(nums)