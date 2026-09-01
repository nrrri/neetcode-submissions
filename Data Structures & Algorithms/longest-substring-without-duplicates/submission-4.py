class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest = 0
        # checkStr = ""
        # for char in range(len(s)):
        #     print(f"check str: {s[char]} | {checkStr}")
        #     print(f"check str: {s[char] in checkStr}")
        #     if s[char] in checkStr:
        #         longest = max(len(checkStr),longest)
        #         checkStr = ""   
        #     checkStr += s[char]
        # longest = max(len(checkStr),longest)
            
        # return longest
        """
        the problem of this is not hte set, so it doen not store ' '
        """

        charSet = set()
        left = 0 # left position
        longest = 0
        for right in range (len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1 # move left until find the duplicate
            charSet.add(s[right])
            print(len(charSet),right-left +1)
            longest = max(longest, len(charSet))
        return longest

        """
        # Set & sliding window
        1. what doest it want?
            - return in number of the longest
        2. how to start
            - put left, and right to store position
            - expand and store each right and check if there is in set
            - if not -> keep expanding (the length is longer)
                - update longest
            - if exist -> remove left until found the duplicate (the length is shorter)
        3. what are the conditions?
            - the duplicate might not be at the most left
            - the longest does not mean the latest length

        """