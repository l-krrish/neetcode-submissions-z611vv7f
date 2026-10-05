class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        book={}
        for i in range(len(nums)):
            if nums[i] not in book:
                book[nums[i]]=1
            else:
                book[nums[i]]+=1
        
        for k,v in book.items():
            if v>(len(nums)/2):
                return k