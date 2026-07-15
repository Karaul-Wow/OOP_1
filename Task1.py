class Student():
    def __init__(self, name, surname, gender) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []

    
class Mentor():
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def __init__(self, name, surname) -> None:
        super().__init__(name, surname)


class Reviewer (Mentor):
    def __init__(self, name, surname) -> None:
        super().__init__(name, surname)


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Петр', 'Петров')

print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []