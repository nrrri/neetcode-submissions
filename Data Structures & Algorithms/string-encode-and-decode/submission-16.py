class Solution:
    def encode(self, strs: List[str]) -> str:
        arr = ""
        for st in strs:
            arr += str(len(st)) + "#" + st
        return arr

    def decode(self, s: str) -> List[str]:
        result, start = [], 0
        # {len}#{word}|{len}#{word}...
        # find # index
        # get length from start -> poundIndex
        # find word from poundIndex+1 -> poundIndex+length+1
        # dont forget to update i to start at the nest word
        # next word (start) = poundIndex + (word)length + 1 
        while start < len(s):
            poundIndex = start
            # poundIndex = index from # -> #
            while s[poundIndex] != "#":
                poundIndex += 1
            length = int(s[start:poundIndex]) # in case if length is more than 1 digit
            result.append(s[poundIndex + 1 : poundIndex + length + 1])
            start = poundIndex + 1 + length

        return result
