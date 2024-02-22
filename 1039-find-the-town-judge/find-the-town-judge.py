class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trusts_count=[0]*(n+1)
        trusted_count=[0]*(n+1)

        for a, b in trust:
            trusts_count[a] += 1
            trusted_count[b] += 1
    
    # Check for the town judge
        for i in range(1, n + 1):
            if trusts_count[i] == 0 and trusted_count[i] == n - 1:
                return i

        return -1