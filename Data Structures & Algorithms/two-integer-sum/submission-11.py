class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creating a hash map
        hash_map = {}   
        for i, num in enumerate(nums):
            diff = target - num
            if(diff in hash_map):
                return [hash_map[diff], i]

            hash_map[num] = i
