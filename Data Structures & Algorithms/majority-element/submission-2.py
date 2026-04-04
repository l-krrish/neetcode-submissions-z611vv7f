class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_set={}
        for i in nums:
            if i not in hash_set:
                hash_set[i]=1
            else:
                hash_set[i]+=1
        
        max_count=0
        max_element=0

        for k,v in hash_set.items():
            if v>max_count:
                max_count=v
                max_element=k
        
        return max_element