class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        # Initialize variables
        a=0
        b=0
        # Iterate through each move and update displacement
        for move in moves:
            if move == 'L':
                a-=1
                b-=1
            elif move=='_':

                a-=1
                b+=1
            elif move == 'R' :
                a+=1
                b+=1

            # Update max_distance if needed
            max_distance = max(abs(a), abs(b))

        return max_distance
