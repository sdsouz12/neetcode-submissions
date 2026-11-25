class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows  = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                currVal=board[r][c]
                if currVal == '.':
                  continue


                b = (r // 3) * 3 + (c // 3)
                if currVal in rows[r] or currVal in cols[c] or currVal in boxes[b]:
                    return False
                else:
                    cols[c].add(currVal)
                    rows[r].add(currVal)
                    boxes[b].add(currVal)

        return True
