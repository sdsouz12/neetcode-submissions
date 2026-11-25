class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      visited ={}

      for number in nums:
        if number in visited:
            return True
        visited[number]= 1 + visited.get(number,0)

      return False

