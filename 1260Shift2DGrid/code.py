class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        N = rows*cols
        shift = k%N
        if shift == 0:
            return grid
        flattened = []
        for y in range(rows):
            for x in range(cols):
                flattened.append(grid[y][x])
        flattened = flattened[-shift:] + flattened[:-shift]
        return  [[ flattened[y*cols + x] for x in range(cols)] for y in range(rows)]
