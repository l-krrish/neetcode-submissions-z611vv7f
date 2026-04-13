class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sol=[]
        ref=len(nums)+1
        for i in range(1,ref):
            if i not in nums:
                sol.append(i)
        return sol