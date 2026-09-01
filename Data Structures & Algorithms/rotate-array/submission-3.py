class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #check if K in len(nums)
        # slice into 2 array
        # before k -> move to the back
        # after k -> shift to the front

        # for i , num in enumerate(nums[:]):
        #     if i < k:
        #         save = num
        #         nums.pop(0)
        #         nums.append(save)
        # NOT EFFICIENT

        # for _ in range(k):
        #     nums.append(nums.pop(0))
        # TIME COMPLEX : O(n*k)
        
        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]
        # THIS WAY THE BEST, TIME COMPLEX = O(n)