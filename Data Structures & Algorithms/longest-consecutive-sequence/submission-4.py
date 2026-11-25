class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        longestSequence = 0

        noDupilcate =set(nums)

        
        for num in noDupilcate:
            if num-1 not in noDupilcate:
                length = 1
                while (num + length) in noDupilcate:
                    length+=1
                longestSequence = max(length, longestSequence)

        return longestSequence
            
            