class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find h from max h1 and h2
        # find w from index of h1 and h2
        # area = min of h * w
        result = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[r], heights[l])

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            result = max(result, area)

        return result
