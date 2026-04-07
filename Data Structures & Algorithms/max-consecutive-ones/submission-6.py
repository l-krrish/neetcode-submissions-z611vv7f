class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result=[list(g) for k,g in groupby(nums,lambda x : x==0) if not k]
        curr=0
        for i in result:
            if len(i)>curr:
                curr=len(i)
        return curr


