class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,columns=len(grid), len(grid[0])
        visit=set()
        islands=0
        res=[]

        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            count=1
            while q:
                row,col=q.popleft()
                directions=[[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    r,c=dr+row,dc+col
                    if(r in range(rows) and c in range(columns) and (r,c) not in visit and grid[r][c] == 1):
                        visit.add((r,c))
                        q.append((r,c))
                        count+=1
            res.append(count)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==1 and (r,c) not in visit:
                    bfs(r,c)
        return max(res) if res else 0