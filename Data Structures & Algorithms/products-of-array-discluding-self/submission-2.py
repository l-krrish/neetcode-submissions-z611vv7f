class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_nums=[0]*len(nums)
        for i in range(len(nums)):
            prod=1
            for j in range(len(nums)):
                if i==j:
                    continue
                prod*=nums[j]
            prod_nums[i]=prod
        
        return prod_nums