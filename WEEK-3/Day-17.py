class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i in (0, len(board)-1) or j in (0, len(board[0])-1)) and board[i][j] == 'O':
                    queue.append((i, j))
        while queue:
            i, j = queue.pop(0)
            if 0<=i<len(board)  and 0<=j<len(board[0]) and board[i][j] == 'O':
                board[i][j] = 'temp'
                queue.append((i+1, j))
                queue.append((i-1, j))
                queue.append((i, j+1))
                queue.append((i, j-1))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'temp':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'  