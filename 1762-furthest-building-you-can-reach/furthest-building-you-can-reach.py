class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        diffs_heap = []  # Min-heap to store the k smallest height differences
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                if ladders > 0:
                    heapq.heappush(diffs_heap, diff)
                    ladders -= 1
                elif diffs_heap and diff > diffs_heap[0]:
                    bricks -= heapq.heappop(diffs_heap)
                    heapq.heappush(diffs_heap, diff)
                else:
                    bricks -= diff
            
            if bricks < 0:
                return i
        
        return len(heights) - 1