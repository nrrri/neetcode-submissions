class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if target == nums[m]:
                return m

            if nums[m] < nums[r]:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else: # nums[l] >= nums[m]
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

# Summary
# x...y/a...b
# l     m   r -> m<r, taget < nums[m] OR taget > b (nums[r]) -> search [x...y]
# 
