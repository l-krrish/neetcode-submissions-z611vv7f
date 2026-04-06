class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        used=[False]*len(nums)

        def dfs(path):
            if len(path)==len(nums):
                result.append(path[:])
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i]=True
                dfs(path)
                path.pop()
                used[i]=False
        dfs([])
        return result