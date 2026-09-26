class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        ans = [] 
        for i in range (len(nums)):
            sum = target - nums[i]
            for j in range (i + 1 , len(nums)):
                if nums[j] == sum:
                    ans.append(j)
                    ans.append(i)
                    return sorted(ans)