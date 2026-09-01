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
        the problem of this is
        when set the new checkStr didn't remove left until find the duplicate
        so when the case like abcbd -> it will return only bd the correct should return cbd
         if s[char] in checkStr:
        #         longest = max(len(checkStr),longest)
        #         checkStr = ""  
        """

        charSet = set() # keet in object {'a','b',...}
        left = 0 # left position
        longest = 0
        for right in range (len(s)): # time complexity = O(n)
            while s[right] in charSet:
                charSet.remove(s[left]) # the length is shorter
                left += 1 # move left until find the duplicate
            charSet.add(s[right]) # the length is longer
            longest = max(longest, len(charSet)) # update the longest
        return longest

        """
        # Set & Sliding window
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
            - use add and remove for set
            - start at left = 0, right = 0 is ok bc charSet has not set yet

        """