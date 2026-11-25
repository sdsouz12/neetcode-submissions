class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd = nums[0]
        maxProd = nums[0]
        finalAns = nums[0]

        for num in nums[1:]:
            temp = min( minProd * num , num , maxProd*num)
            maxProd = max(minProd * num , num , maxProd*num)
            minProd = temp
            finalAns = max( finalAns, maxProd)

        return finalAns