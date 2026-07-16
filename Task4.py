class Student():
    student_list = []

    def __init__(self, name, surname, gender) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.aver_grade = 0
        Student.student_list.append(self)

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
        if n_grade > 0: self.aver_grade = round(self.aver_grade / n_grade, 1)
        return self.aver_grade

    def __str__(self) -> str:
        outstr = '\n'
        outstr = f'{outstr}print(some_student)\n'
        outstr = f'{outstr}Имя: {self.name}\n'
        outstr = f'{outstr}Фамилия: {self.surname}\n'
        outstr = f'{outstr}Средняя оценка за домашние задания: {self.aver_grade}\n'
        outstr = f'{outstr}Курсы в процессе обучения: {", ".join(self.courses_in_progress)}\n'
        outstr = f'{outstr}Завершенные курсы: {", ".join(self.finished_courses)}'
        return outstr
    
    def __gt__(self, other):
        return self.aver_grade > other.aver_grade

    
class Mentor():
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    lecturer_list = []

    def __init__(self, name, surname) -> None:
        super().__init__(name, surname)
        self.grades = {}
        self.aver_grade = 0
        Lecturer.lecturer_list.append(self)

    def __str__(self) -> str:
        outstr = '\n'
        outstr = f'{outstr}print(some_lecturer)\n'
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
        if n_grade > 0: self.aver_grade = round(self.aver_grade / n_grade, 1)
        return self.aver_grade
    
    def __gt__(self, other):
        return self.aver_grade > other.aver_grade


class Reviewer (Mentor):

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
        outstr = '\n'
        outstr = f'{outstr}print(some_reviewer)\n'
        outstr = f'{outstr}Имя: {self.name}\n'
        outstr = f'{outstr}Фамилия: {self.surname}'
        return outstr


student_01 = Student('Иван','Иванов', 'М')
student_01.courses_in_progress += ['Java', 'Python', 'SQL']
student_01.finished_courses += ['C++', '1C']
student_01.grades.update({'C++': [8, 9], '1C': [7, 8]})
student_01.aver_grade_calc()

student_02 = Student('Петр','Петров', 'М')
student_02.courses_in_progress += ['1C', 'Python', 'SQL']
student_02.finished_courses += ['C++', 'Java']
student_02.grades.update({'C++': [7, 8], 'Java': [6, 7]})
student_02.aver_grade_calc()


lecturer_01 = Lecturer('Сидор', 'Сидоров')
lecturer_01.courses_attached += ['Python', 'C++']
lecturer_01.grades.update({'C++': [7, 8]})
lecturer_01.aver_grade_calc()

lecturer_02 = Lecturer('Василий', 'Васильев')
lecturer_02.courses_attached += ['SQL', '1C']
lecturer_02.grades.update({'1C': [8, 9]})
lecturer_02.aver_grade_calc()


reviewer_01 = Reviewer('Макар', 'Макаров')
reviewer_01.courses_attached += ['Python', 'C++']
reviewer_02 = Reviewer('Дмитрий', 'Дмитриев')
reviewer_02.courses_attached += ['SQL']

reviewer_01.rate_hw(student_01, 'Python', 9)
reviewer_01.rate_hw(student_01, 'Python', 10)
reviewer_01.rate_hw(student_01, 'C++', 10)
reviewer_01.rate_hw(student_02, 'Python', 8)
reviewer_01.rate_hw(student_02, 'Python', 9)
reviewer_01.rate_hw(student_01, '1C', 10)


reviewer_02.rate_hw(student_01, 'SQL', 8)
reviewer_02.rate_hw(student_01, 'SQL', 8)
reviewer_02.rate_hw(student_02, 'SQL', 9)
reviewer_02.rate_hw(student_02, 'SQL', 10)

student_01.rate_lecture(lecturer_01, 'Python', 5)
student_01.rate_lecture(lecturer_01, '1С', 5)
student_01.rate_lecture(lecturer_01, 'Java', 5)
student_01.rate_lecture(lecturer_02, 'SQL', 7)
student_02.rate_lecture(lecturer_01, 'Python', 8)
student_02.rate_lecture(lecturer_02, 'SQL', 8)

print(student_01)
print(student_02)
print(lecturer_01)
print(lecturer_02)
print(reviewer_01)
print(reviewer_02)

print(f"\nСтудент {student_01.name} {student_01.surname} успешнее чем {student_02.name} {student_02.surname}? - {student_01 > student_02}")
print(f"\nЛектор {lecturer_01.name} {lecturer_01.surname} успешнее чем {lecturer_02.name} {lecturer_02.surname}? - {lecturer_01 > lecturer_02}")



def average_grade_course(person_list, course):
    course_aver_grade = 0
    n_grade = 0
    for person in person_list:
        if course in person.grades:
            course_aver_grade += sum(person.grades[course])
            n_grade += len(person.grades[course])
    if n_grade > 0: course_aver_grade = round(course_aver_grade/n_grade, 1)
    return course_aver_grade

def average_grade_course_stud(student_list, course):
    return average_grade_course(student_list, course)

student_list = Student.student_list
course = 'Python'

print (f'\nСредняя оценка за домашние задания по всем студентам в рамках курса {course} - {average_grade_course_stud(student_list, course)}')

lecturer_list = Lecturer.lecturer_list

def average_grade_course_lecturer(lecturer_list, course):
    return average_grade_course(lecturer_list, course)

print (f'\nСредняя оценка за лекции всех лекторов в рамках курса {course} - {average_grade_course_stud(lecturer_list, course)}')

course = 'SQL'

print (f'\nСредняя оценка за домашние задания по всем студентам в рамках курса {course} - {average_grade_course_stud(student_list, course)}')
print (f'\nСредняя оценка за лекции всех лекторов в рамках курса {course} - {average_grade_course_stud(lecturer_list, course)}')
