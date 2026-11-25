class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex ={}

        for i,char in enumerate(s):
            lastIndex[char] = i


        result =[]
        size , end = 0,0

        for i, char in enumerate(s):
            size += 1
            end = max(end,lastIndex[char])

            if end == i:
                result.append(size)
                size=0
        return result