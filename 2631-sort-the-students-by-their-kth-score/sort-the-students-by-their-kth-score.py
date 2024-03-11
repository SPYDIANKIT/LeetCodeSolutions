class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        for i in range(len(score)):
            max_idx = i
            for j in range(i+1, len(score)):
                if score[j][k] > score[max_idx][k]:
                    max_idx = j
            score[i], score[max_idx] = score[max_idx], score[i]

        
        return score