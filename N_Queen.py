def N_Queen(n):
  board=[[0]*n for _ in range(n)]
  def check_is_safe(row,col):
    #check column
    for i in range(row):
      if board[i][col]==1:
        return False
    for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
      if board[i][j]==1:
        return False
    for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
      if board[i][j]==1:
        return False
    return True
  def solve(row):
    if row==n:
      return True
    for col in range(n):
      if check_is_safe(row,col):
        board[row][col]=1
        if solve(row+1):
          return True
        board[row][col]=0
    return False
  if solve(0):
    for row in board:
      print(row)
  else:
      print("No solution exists")
N_Queen(8)

    
  

