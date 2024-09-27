class Solution:
   def getTotalIsles(self, grid: list[list[str]]) -> int:
      if not grid:
          return 0
      rows,cols = len(grid),len(grid[0])
   def dfs(r,c):
       if r<0 or r >= rows or c<0 or c>= cols or grid[r][c] == 'w':
          return    
          
       grid[r][c] = 'w'
       dfs(r+1,c)
       dfs(r-1,c)
       dfs(r,c+1)
       dfs(r,c-1)

   island_count = 0
   for r in range(rows):
      for c in range(cols):
      if  grid[r][c] == 'U':
         dfs(r,c)
         island_count += 1
   return island_count

      
         
    
