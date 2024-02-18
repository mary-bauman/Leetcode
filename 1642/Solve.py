import ast
from heapq import *
from typing import *

def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
    n = len(heights)
    heap = []
    brickSum = 0
    for i in range(1, n):
        difference = heights[i] - heights[i-1]
        if difference > 0:
            heappush(heap, difference)
            if len(heap) > ladders:
                brickSum += heappop(heap)
                if brickSum > bricks:
                    return i-1
    return n-1

with open('1642/in.txt') as f:
    heights = ast.literal_eval(f.readline())
    bricks = int(f.readline())
    ladders = int(f.readline())
    print(furthestBuilding(heights, bricks, ladders))