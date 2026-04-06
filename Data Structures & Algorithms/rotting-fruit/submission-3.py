from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        col=len(grid[0])
        queue=deque()
        fresh_fruit=0

        for r in range(rows):
            for c in range(col):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh_fruit+=1
        
        minutes=0

        while queue and fresh_fruit >0:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr=r+dr
                    nc=c+dc

                    if 0 <= nr < rows and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc]=2
                        queue.append((nr,nc))
                        fresh_fruit-=1
            minutes+=1
        return minutes if fresh_fruit==0 else -1