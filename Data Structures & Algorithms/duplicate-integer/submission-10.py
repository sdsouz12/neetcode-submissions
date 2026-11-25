class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      visited = set()

      for number in nums:
        if   number in visited:
            return True
        else:
            visited.add(number)
      return False