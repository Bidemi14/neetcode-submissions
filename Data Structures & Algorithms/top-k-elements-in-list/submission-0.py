class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for x in nums :
            if x in group:
                group[x] = group[x] + 1
            else:
                group[x]= 1
                 
       
        return sorted(group, key=lambda x: group[x], reverse=True)[:k]


