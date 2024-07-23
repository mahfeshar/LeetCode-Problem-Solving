class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        repColms = {i: [0] * 10 for i in range(10)}
        for row in range(len(board)):
            repRow = set()
            for col in range(len(board[row])):
                if board[row][col] !=  ".":
                    if board[row][col] not in repRow:
                        repRow.add(board[row][col])
                    else:
                        return False
                    
                    if repColms[col][int(board[row][col])] == 0:
                        repColms[col][int(board[row][col])] = 1
                    else:
                        return False
                if row % 3 == 0 and col % 3 == 0:
                    repSqr = set()
                    for i in range(3):
                        for j in range(3):
                            if board[row + i][col + j] not in repSqr:
                                if board[row + i][col + j] == '.':
                                    continue
                                repSqr.add(board[row + i][col + j])
                            else:
                                return False
        return True