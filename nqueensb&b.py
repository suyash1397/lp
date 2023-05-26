#!/usr/bin/env python
# coding: utf-8

# In[3]:


def solve(board, row, cols, ndiag, rdiag, asf):
    if row == len(board):
        valid_config = [[0 for _ in range(len(board))] for _ in range(len(board))]
        if asf.strip() != "":
            for pos in asf.split(", "):
                if pos.strip() != "":
                    r, c = map(int, pos.split("-"))
                    valid_config[r][c] = 1
        return [valid_config]
    
    valid_configs = []
    for col in range(len(board[0])):
        if cols[col] == False and ndiag[row + col] == False and rdiag[row - col + len(board) - 1] == False:
            board[row][col] = True
            cols[col] = True
            ndiag[row + col] = True
            rdiag[row - col + len(board) - 1] = True
            valid_configs.extend(solve(board, row + 1, cols, ndiag, rdiag, asf + str(row) + "-" + str(col) + ", "))
            board[row][col] = False
            cols[col] = False
            ndiag[row + col] = False
            rdiag[row - col + len(board) - 1] = False

    return valid_configs


N = 4
cols = [False] * N
ndiag = [False] * (2 * N - 1)
rdiag = [False] * (2 * N - 1)
board = [[False for _ in range(N)] for _ in range(N)]

valid_configs = solve(board, 0, cols, ndiag, rdiag, "")

# Print the valid configurations as matrices
for config in valid_configs:
    for row in config:
        print(row)
    print()


# In[ ]:




