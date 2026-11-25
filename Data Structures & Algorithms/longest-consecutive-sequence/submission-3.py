class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        noDuplicates = set(nums)

        for num in nums:
            if (num -1) not in noDuplicates:
                currLen = 0
                while(num + currLen) in noDuplicates:
                    currLen += 1
                longest = max(currLen,longest)
        return longest
