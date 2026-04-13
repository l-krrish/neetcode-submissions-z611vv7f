class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sol=[]
        for i in range(1,len(nums)+1):
            sol.append(i)
        for num in nums:
            if num in sol:
                sol.remove(num)
        return sol
