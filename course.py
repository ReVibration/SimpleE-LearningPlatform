class Course:
    def __init__(self, title, description, max_capacity=30):
        # title: course title
        # description: course description
        # max_capacity: maximum number of students (default 30)
        # instructor: initially None
        # students: empty list to track enrolled students
        # completed_students: empty list to track students who completed the course
        self.title = title
        self.description = description
        self.instructor = None
        self.max_capacity = max_capacity
        self.students = []
        self.completed_students = []
        pass
    
    def add_student(self, student):
        # Add a student to the course
        # - Return False if the course is at max capacity (len(self.students) >= self.max_capacity)
        # - Return False if student is already in self.students
        # - Add student to self.students list and return True on success
        if len(self.students) >= self.max_capacity:
            return False
        if student in self.students:
            return False
        self.students.append(student)
        return True
        pass
    
    def remove_student(self, student):
        # Remove a student from the course
        # - Return False if student is not in self.students
        # - Remove student from self.students list and return True on success
        if student in self.students:
            self.students.remove(student)
            return True
        return False
        pass
    
    def mark_completed(self, student):
        # Mark a student as having completed the course
        # - Return False if student is not in self.students
        # - Remove student from self.students list
        # - Add student to self.completed_students list
        # - Return True on success
        if student in self.students:
            self.students.remove(student)
            self.completed_students.append(student)
            return True
        return False
        pass
    
    def assign_instructor(self, instructor):
        # Assign an instructor to the course
        # - Set self.instructor to the provided instructor
        # - Return True (always succeeds)
        self.instructor = instructor
        return True
        pass
