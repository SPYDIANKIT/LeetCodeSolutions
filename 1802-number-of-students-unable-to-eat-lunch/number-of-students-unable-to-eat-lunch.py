class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = [0, 0]
        
        # Count the number of students who prefer each type of sandwich
        for student in students:
            count[student] += 1
        
        # Iterate through the sandwiches
        for sandwich in sandwiches:
            # If there are no more students who prefer the current type of sandwich, break the loop
            if count[sandwich] == 0:
                break
            
            # Reduce the count of students who prefer the current type of sandwich
            count[sandwich] -= 1
        
        # Return the number of students who couldn't eat
        return sum(count)