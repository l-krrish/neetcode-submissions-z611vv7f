class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sol=[]
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
            else:
                sol.append(nums[i])
        
        for j in range(c):
            sol.append(0)
        nums[:]=sol
        return nums

        