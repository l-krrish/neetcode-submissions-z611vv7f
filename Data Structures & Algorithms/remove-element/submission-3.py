class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_rem=[]
        for i in nums:
            if i!=val:
                nums_rem.append(i)
        
        nums[:]=nums_rem

        return len(nums)