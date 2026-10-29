class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        result = 0
        # find max l and r
        # h = min(height[l],height[r])-height[i]
        # h can trap the water
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]

        return result
