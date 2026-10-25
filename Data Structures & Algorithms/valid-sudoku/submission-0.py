class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # all x not duplicated
        # all y not duplicated (same but reverse matrix)
        # [x:x+3,y:y+3] not duplicated, [0-2,3-5,6-8]
        result = True
        # check row
        for i in board:
            row = set()
            for j in i:
                if j == '.':
                    continue
                if j in row:
                    print(j,row)
                    result = False
                row.add(j)
        # check column
        rotated_board = [list(row)[::-1] for row in zip(*board)]
        for i in rotated_board:
            col = set()
            for j in i:
                if j == '.':
                    continue
                if j in col:
                    result = False
                col.add(j)

        # check 3x3
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for row in board[i:i+3]:
                    for val in row[j:j+3]:
                        if val == '.':
                            continue
                        if val in seen:
                            result = False
                        seen.add(val)

        return result
