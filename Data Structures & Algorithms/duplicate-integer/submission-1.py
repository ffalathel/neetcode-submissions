class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for number in nums:
            if number not in duplicates:
                duplicates.add(number)
            else:
                return True
        return False

        