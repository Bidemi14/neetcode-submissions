class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for x in strs:
            key = ''.join(sorted(x))
            if key in group:
                group[key].append(x)
            else:
                group[key] = [x]
        return list(group.values())