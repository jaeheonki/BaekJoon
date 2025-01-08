n, m = map(int, input().split())
board = []
result = []

board = [list(input()) for _ in range(n)]

for i in range(n-7):
  for j in range(m-7):
    is_black = 0
    is_white = 0

    for a in range(i, i+8):
      for b in range(j, j+8):
        if (a + b) % 2 == 0:
          if board[a][b] != 'B':
            is_black += 1
          if board[a][b] != 'W':
            is_white += 1
        else:
          if board[a][b] != 'W':
            is_black += 1
          if board[a][b] != 'B':
            is_white += 1

    result.append(is_black)
    result.append(is_white)

print(min(result))