class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       hashmap = {}
       for index , value in enumerate(nums):
        comp = target - value
        if (comp in hashmap):
            return hashmap[comp], index
        else :
            hashmap[value] = index
       return False
