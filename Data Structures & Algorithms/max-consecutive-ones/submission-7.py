class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count = 0   # max streak
        c = 0            # current streak
        
        for i in range(len(nums)):
            if nums[i] == 1:
                c += 1
                if c > curr_count:
                    curr_count = c
            else:
                c = 0
        
        return curr_count