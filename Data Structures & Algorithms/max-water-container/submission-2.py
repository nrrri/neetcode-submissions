class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find h from max h1 and h2
        # find w from index of h1 and h2
        # area = min of h * w
        area = 0
        l,r = 0, len(heights) -1
        while l < r:
            w = r-l
            h = min(heights[r],heights[l])

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            area = max(area,w*h)

        return area
