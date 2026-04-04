class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map={}
        for i in nums:
            if i not in frequency_map:
                frequency_map[i]=1
            else:
                frequency_map[i]+=1
        sorted_fm_items=sorted(frequency_map.items(),key=lambda item:item[1],reverse=True)
        sorted_fm=dict(sorted_fm_items)

        L=[]
        L1=list(sorted_fm.keys())
        for i in range(k):
            L.append(L1[i])
        
        return L