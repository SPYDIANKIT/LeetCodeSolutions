class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        dp = [float('inf')] * n
        dp[src] = 0

        # Iterate k times to update dp array
        for _ in range(k + 1):
            temp = dp[:]
            for flight in flights:
                from_city, to_city, price = flight
                if dp[from_city] != float('inf'):
                    temp[to_city] = min(temp[to_city], dp[from_city] + price)
            dp = temp

        # Return cost to reach destination if reachable, else -1
        return dp[dst] if dp[dst] != float('inf') else -1