class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        for i,num in enumerate(numbers):
            searchElement = target - num
            left = i+1
            right = len(numbers) -1
            while(left<=right):
                mid = left+(right-left)//2

                if(numbers[mid]>searchElement):
                    right = mid-1
                elif (numbers[mid]<searchElement):
                    left = mid+1
                else:
                    return [i+1, mid+1]