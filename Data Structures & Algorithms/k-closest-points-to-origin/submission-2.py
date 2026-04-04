import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hash_map={}
        for i in points:
            distance = math.sqrt(i[0]**2 + i[1]**2)
            hash_map[tuple(i)]=distance
        
        hash_map=dict(sorted(hash_map.items(), key=lambda item: item[1]))
        values=[]
        for i in range(k):
            keys = list(hash_map.keys())
            values.append(list(keys[i]))
        return values

