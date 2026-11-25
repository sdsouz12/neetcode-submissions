class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        prefix_product = 1
        postfix_product = 1

        for i,num in enumerate(nums):
            result[i] = prefix_product
            prefix_product = num * prefix_product

        for i in range(len(result) - 1, -1, -1):
            result[i]= postfix_product * result [i]
            postfix_product = postfix_product * nums[i]

        return result
