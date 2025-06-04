while True:
      n,k=map(int,input().split())
      if n==k==-1:
          break
      board=[]
      for i in range(n):
            s=input()
            board.append(s)
      count=0
      def backtrack(mask,row,g):
          global count
          if g == k:
              count += 1
              return
          if n-row<k-g:
              return
          if row>=n:
              return
          backtrack(mask, row + 1, g)
          for j in range(n):
              if not mask&(1<<j):
                  if board[row][j]=="#":
                     backtrack(mask|(1<<j),row+1,g+1)

      backtrack(0,0,0)
      print(count)






