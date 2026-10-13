class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_nums = {}
        for i in range(len(nums)):
            if target - nums[i] in my_nums:
                return [my_nums[target-nums[i]], i]
            my_nums[nums[i]] = i
            i+=1
        return 0

