class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check presence of digit in rows
        for idx_row, row in enumerate(board):
            seen = set()
            for string in row:
                if string == '.':
                    continue
                elif string in seen:
                    return False
                else:
                    seen.add(string)
        for idx_col in range(9):
            seen = set()
            for string in list(zip(*board))[idx_col]:
                if string == '.':
                    continue
                elif string in seen:
                    return False
                else:
                    seen.add(string)

        for idx_box in range(9):
            seen = set()
            print("box", idx_box)
            for idx in range(9):
                row = (idx_box//3)*3 + idx//3
                col = (idx_box%3)*3 + idx%3
                print(row,col)
                string = board[row][col]
                if string == '.':
                    continue
                elif string in seen:
                    return False
                else:
                    seen.add(string)
        return True