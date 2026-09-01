class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for ch in strs:
            char = "".join(sorted(ch))
            if char in group :
                group[char].append(ch)
            else:
                group[char] = [ch]
        return list(group.values()) # list makes it array