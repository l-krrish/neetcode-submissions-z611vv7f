class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new=[]
        for i in nums:
            if i!=val:
                new.append(i)
        nums[:]=new
        return len(new)