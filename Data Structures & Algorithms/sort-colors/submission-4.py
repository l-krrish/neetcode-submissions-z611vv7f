class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hash_map={0:0,1:0,2:0}

        for num in nums:
            hash_map[num]+=1
        i=0
        for color in [0,1,2]:
            for _ in range(hash_map[color]):
                nums[i]=color
                i+=1
            
        