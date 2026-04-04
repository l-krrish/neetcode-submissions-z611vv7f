class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[]
        for i in range(len(nums)):
            curr=nums[:i] + nums[i+1:]
            p=1
            for x in curr:
                p=p*x
            prod.append(p)
        return prod