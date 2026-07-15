class Student():
    def __init__(self, name, surname, gender) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.aver_grade = 0

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        lecturer.aver_grade_calc()

    def aver_grade_calc(self):
        self.aver_grade = 0
        n_grade = 0
        for grade_key in self.grades:
            self.aver_grade += sum(self.grades[grade_key])
            n_grade += len(self.grades[grade_key])
        if n_grade > 0: self.aver_grade = self.aver_grade / n_grade
        return self.aver_grade

    def __str__(self) -> str:
        outstr = f'print(some_student)\n'
        outstr = f'{outstr}Имя: {self.name}\n'
        outstr = f'{outstr}Фамилия: {self.surname}\n'
        outstr = f'{outstr}Средняя оценка за домашние задания: {self.aver_grade}\n'
        outstr = f'{outstr}Курсы в процессе обучения: {", ".join(self.courses_in_progress)}\n'
        outstr = f'{outstr}Завершенные курсы: {", ".join(self.finished_courses)}'
        return outstr

    
class Mentor():
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def __init__(self, name, surname) -> None:
        super().__init__(name, surname)
        self.grades = {}
        self.aver_grade = 0

    def __str__(self) -> str:
        outstr = f'print(some_lecturer)\n'
        outstr = f'{outstr}Имя: {self.name}\n'
        outstr = f'{outstr}Фамилия: {self.surname}\n'
        outstr = f'{outstr}Средняя оценка за лекции: {self.aver_grade}'
        return outstr

    def aver_grade_calc(self):
        self.aver_grade = 0
        n_grade = 0
        for grade_key in self.grades:
            self.aver_grade += sum(self.grades[grade_key])
            n_grade += len(self.grades[grade_key])
        if n_grade > 0: self.aver_grade = self.aver_grade / n_grade
        return self.aver_grade


class Reviewer (Mentor):
    def __init__(self, name, surname) -> None:
        super().__init__(name, surname) 

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        student.aver_grade_calc()

    def __str__(self) -> str:
        outstr = f'print(some_reviewer)\n'
        outstr = f'{outstr}Имя: {self.name}\n'
        outstr = f'{outstr}Фамилия: {self.surname}'
        return outstr



lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Петр', 'Петров')
student = Student('Ольга', 'Алёхина', 'Ж')

student.courses_in_progress += ['Python', 'Java']
student.finished_courses += ['Введение в программирование']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

student.rate_lecture(lecturer, 'Python', 7)
student.rate_lecture(lecturer, 'Python', 8)
reviewer.rate_hw(student, 'Python', 8)
reviewer.rate_hw(student, 'Python', 9)

print(reviewer)
print(lecturer)
print(student)

student_02 = Student('Сидор', 'Сидоров', 'М')
student_02.courses_in_progress += ['Python', 'Java']
reviewer.rate_hw(student_02, 'Python', 8)
reviewer.rate_hw(student_02, 'Python', 9)

print(f"{student.name} {student.surname} успешнее чем {student_02.name} {student_02.surname}? - {student.aver_grade > student_02.aver_grade}")

lecturer_02 = Lecturer('Макар', 'Макаров')
lecturer_02.courses_attached += ['Python', 'C++']
student_02.rate_lecture(lecturer_02, 'Python', 8)
student_02.rate_lecture(lecturer_02, 'Python', 9)

print(f"{lecturer.name} {lecturer.surname} успешнее чем {lecturer_02.name} {lecturer_02.surname}? - {lecturer.aver_grade > lecturer_02.aver_grade}")