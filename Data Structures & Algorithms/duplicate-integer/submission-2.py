class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = set()
        amount = 0
        for n in nums:
            if n in storage:
                return True 
            else:
                storage.add(n)
        return False
        