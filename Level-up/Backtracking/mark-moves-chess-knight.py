from collections import deque

# Chess board :
board = [[0] * 8 for _ in range(8)]

# Valid move checking function :
def is_valid(x, y) -> bool:
    return 0 <= x < 8 and 0 <= y < 8

# Marking function :
def mark_moves(start_x, start_y, step):
    # Possible moves for the chess knight :
    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    # Adding the next valid moves in queue :
    q = deque([(start_x, start_y)])
    # visited 2d array for tracking all the x,y
    visited = [[False] * 8 for _ in range(8)]
    visited[start_x][start_y] = True
    # Traversing the queue :
    while q:
        current_X, current_Y = q.popleft()
        # Calculating all possible valid moves :
        for i in range(8):
            new_x, new_y = current_X + dx[i], current_Y + dy[i]
            # Marking the board & adding the next moves to queue when condition satisfies :
            if is_valid(new_x, new_y) and board[new_x][new_y] == 0 and not visited[new_x][new_y]:
                board[new_x][new_y] = step + 1
                q.append((new_x, new_y))
                visited[new_x][new_y] = True
        # Incrementing the step for next traversal :
        step += 1

# Input stream :
start_x, start_y = [5, 5]
mark_moves(start_x - 1, start_y - 1, 0)

# Printing the board to see the result
for row in board:
    print(row)
