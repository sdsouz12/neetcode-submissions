class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # lookup O(1)
        

        for index,num in enumerate(nums):
            difference = target - num 
            if difference in seen:
                return [seen[difference], index]
            seen[num] = index
        return False

            