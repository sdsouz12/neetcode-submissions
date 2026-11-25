class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for item in intervals[1:]:
            last = res[-1]
            if item[0] <= last[1]:
                #overlap
                last[1] = max(last[1], item[1])
            else:
                res.append(item)

        return res
        