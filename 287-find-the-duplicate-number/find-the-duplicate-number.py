class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast, entry = 0, 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while slow != entry:
                    slow = nums[slow]
                    entry = nums[entry]
                return entry
        return None
        