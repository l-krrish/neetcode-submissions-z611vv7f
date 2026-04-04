class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_need=[]
        for i in nums:
            if i!=val:
                nums_need.append(i)

        nums[:]=nums_need
        return len(nums)