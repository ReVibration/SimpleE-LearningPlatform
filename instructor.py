from course import Course

class Instructor:
    def __init__(self, name, email, expertise):
        # Initialize instance attributes:
        # - name: instructor's name
        # - email: instructor's email
        # - expertise: list or string of instructor's areas of expertise
        # - courses: empty list to track courses the instructor is teaching
        self.name = name
        self.email = email
        self.expertise = expertise
        self.courses = []
        pass
    
    def assign_to_course(self, course):
        # Assign the instructor to a course
        # - Use course.assign_instructor(self) to assign the instructor to the course
        # - Add the course to self.courses list
        # - Return True (always succeeds)
        course.assign_instructor(self)
        self.courses.append(course)
        return True
        pass
