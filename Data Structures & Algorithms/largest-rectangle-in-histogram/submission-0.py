class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = [] #pair :startIndex,height

        for index, h in enumerate(heights):
            start = index
            while stack and stack[-1][1] > h:
                startIndex, height = stack.pop()

                maxArea = max(maxArea ,(height * (index - startIndex)))
                start = startIndex 
            stack.append((start,h))


        for index,height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))
        return maxArea
