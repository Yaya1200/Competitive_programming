class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        count = 0
        j = 0
        while(True):
            if students[i] == sandwiches[j]:
                students = students[:i] + students[i+1:]
                count =0
                j += 1
            else:
                count += 1    
            i += 1
            if count == len(students)+1:
                return len(students)
            if len(students) == 0:
                return 0
            i =  i % len(students)

