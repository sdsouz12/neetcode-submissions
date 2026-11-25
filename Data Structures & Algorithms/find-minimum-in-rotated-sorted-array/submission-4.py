class Solution:
    def findMin(self, nums: List[int]) -> int:
        left =0
        right = len(nums) -1
        ans= nums[0]

        # if len(nums) == 0 :
        #     return nums[0]
        
        while(left <= right):
            if(nums[left] <= nums[right]):
                ans = min( nums[left], ans)
                break
            mid = (left+right)//2

            ans = min (nums[mid],ans)
            if( nums[left] <= nums[mid]):
                left = mid +1
            else:
                right = mid-1

        return ans

