class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      visited =[]

      for number in nums:
        if number in visited:
            return True
        visited.append(number)

      return False

