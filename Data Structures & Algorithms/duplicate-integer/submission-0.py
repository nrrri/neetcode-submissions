class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = []
        for num in nums:
            print(store)
            if num in store:
                print('dup')
                return True
            store.append(num)
        return False