class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group = {}
        # for ch in strs:
        #     char = "".join(sorted(ch))
        #     if char in group :
        #         group[char].append(ch)
        #     else:
        #         group[char] = [ch]
        # return list(group.values()) # list makes it array
        ### --------------------------------
        # key = store each letter in arr (0,0,1,...) 26 values and value = strs
        # if it has the same pattern -> append str into that key
        # key -> tuple bc has to make it unchangeable, syntax = (0,0,1,...)
        # ord(c) - ord('a') make 'a' start at 0
        # Faster
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # create 26 array with value = 0 first
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())