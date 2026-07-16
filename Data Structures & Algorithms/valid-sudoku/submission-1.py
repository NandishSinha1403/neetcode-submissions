class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return checkRow(board) and checkCol(board) and checkBox(board) 

def checkRow(board):
    for i in board:
        seen = set()
        for j in i:
            if j == ".":
                continue
            if j in seen:
                return False 
            else :
                seen.add(j)
    return True

def checkCol(board):
    for i in range(9):
        seen2 = set()
        for j in board:
            if j[i] == ".":
                continue
            if j[i] in seen2:
                return False
            else :
                seen2.add(j[i])
    return True

def checkBox(board):
    for i in range(0,7,3):
        for j in range (0,7,3):
            seen3 = set()

            for r in range(3):
                for c in range(3):
                    if board[i+r][j+c] == ".":
                        continue
                    if board[i+r][j+c] in seen3:
                        return False 
                    else :
                        seen3.add(board[i+r][j+c])
    return True 



