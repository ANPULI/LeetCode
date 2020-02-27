class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if lookup.get(nums[i], -1) == -1:
                lookup[diff] = i
            else:
                return [lookup[nums[i]], i]