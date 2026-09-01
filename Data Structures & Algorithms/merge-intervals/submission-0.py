class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0]) # i[0] means sort by start val
        res = [intervals[0]]
        for start, end in intervals:
            lastEnd = res[-1][1] # -1 means last
            if start <= lastEnd:
                res[-1][1] = max(lastEnd,end)
            else:
                res.append([start,end])
        return res
        