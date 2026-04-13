class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        for i in nums:
            curr=i
            if nums.count(curr)>n//2:
                return curr