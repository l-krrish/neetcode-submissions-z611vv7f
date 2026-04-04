class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map={}
        
        for i in nums:
            if i not in frequency_map:
                frequency_map[i]=1
            else:
                frequency_map[i]+=1
        
        sorted_items_desc = sorted(frequency_map.items(), key=lambda item: item[1], reverse=True)
        sorted_dict_desc = dict(sorted_items_desc)
        L=[]
        L1=list(sorted_dict_desc.keys())
        for i in range(k):
            L.append(L1[i])

        
        return L