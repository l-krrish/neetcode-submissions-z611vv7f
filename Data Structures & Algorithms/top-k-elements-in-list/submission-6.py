class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        anagram_map={}
        for i in nums:
            if i not in anagram_map:
                anagram_map[i]=1
            else:
                anagram_map[i] += 1
        sorted_items_desc = sorted(anagram_map.items(), key=lambda item: item[1], reverse=True)

        L=[]
        for j in range(k):
            first_value = next(iter(anagram_map.values()))
            L.append(sorted_items_desc[j][0])
        return L
        