class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade_lec):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lec:
                lecturer.grades_lec[course] += [grade_lec]
            else:
                lecturer.grades_lec[course] = [grade_lec]
        else:
            return 'Ошибка'

    def _average_rating_hw(self):  # средняя оценка за домашнее задание
        sum_grade = 0
        len_grade = 0
        for courses, grad in self.grades.items():
            for value in grad:
                sum_grade += value
            len_grade += len(grad)
        if len_grade == 0:
            return 'Оценок нет'
        else:
            return round(sum_grade / len_grade, 1)

    def average_rating_course_hw(self, course):  # оценки по курсу и их количество
        sum_grade_course = 0
        len_grade_course = 0
        for courses, grad in self.grades.items():
            if course == courses:
                sum_grade_course += sum(self.grades[courses])
                len_grade_course += len(self.grades[courses])
        return sum_grade_course, len_grade_course

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за домашнии задания: {self._average_rating_hw()}\n" \
              f"Курс в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
              f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return res

    def __lt__(self, other):  # сравнение студентов по средней оценке за домашнее задание
        if not isinstance(other, Student):
            print('Не относиться к классу Student')
            return
        return self._average_rating_hw() < other._average_rating_hw()


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lec = {}

    def _average_rating_l(self):
        sum_grade = 0
        len_grade = 0
        for course, grad in self.grades_lec.items():
            for value in grad:
                sum_grade += value
            len_grade += len(grad)
        return round(sum_grade / len_grade, 1)

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за лекции: {self._average_rating_l()}"
        return res

    def __lt__(self, other):  # сравнение лекторов по средней оценке за лекции
        if not isinstance(other, Lecturer):
            print('Не относиться к классу Lecturer')
            return
        return self._average_rating_l() < other._average_rating_l()

    def average_rating_course_l(self, course):  # оценки за лекции и их количество
        sum_grade_course_l = 0
        len_grade_course_l = 0
        for courses, grad in self.grades_lec.items():
            if course == courses:
                sum_grade_course_l += sum(self.grades_lec[courses])
                len_grade_course_l += len(self.grades_lec[courses])
        return sum_grade_course_l, len_grade_course_l


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n"
        return res


print('проверяем работу программы')
print()
# создаём студентов
student_1 = Student('Алексей', 'Иванов', 'Boy')
student_1.finished_courses += ['1c']
student_1.courses_in_progress += ['Python', 'Git']

student_2 = Student('Алёна', 'Смирнова', 'girl')
student_2.finished_courses += ['C+', 'Java']
student_2.courses_in_progress += ['Python', 'Git', 'JS']
# создаём лекторов
lecturer_1 = Lecturer('Евгений', 'Позеров')
lecturer_1.courses_attached += ['Python', 'JS']

lecturer_2 = Lecturer('Евгения', 'Позерова')
lecturer_2.courses_attached += ['Git', 'JS', 'Python']
# создаём ревьюверов
reviewer_1 = Reviewer('Дмитрий', 'Александров')
reviewer_1.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Александр', 'Дмитриев')
reviewer_2.courses_attached += ['Python', 'Git', 'JS']

# ревьюверы ставят оценки за дз
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_2, 'Git', 5)

reviewer_2.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 3)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'JS', 5)

# студенты ставят оценки лекторам
student_1.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_1, 'JS', 9)
student_1.rate_lecture(lecturer_2, 'Git', 6)
student_1.rate_lecture(lecturer_2, 'Python', 7)
student_1.rate_lecture(lecturer_2, 'JS', 8)

student_2.rate_lecture(lecturer_1, 'Python', 7)
student_2.rate_lecture(lecturer_1, 'JS', 8)
student_2.rate_lecture(lecturer_2, 'Git', 9)
student_2.rate_lecture(lecturer_2, 'Python', 5)
student_2.rate_lecture(lecturer_2, 'JS', 10)

print('Информация о 1-ом студенте')
print(student_1)
print()

print('Информация о 2-ом студенте')
print(student_2)
print()

print('Информация о 1-ом лекторе')
print(lecturer_1)
print()

print('Информация о 2-ом лекторе')
print(lecturer_2)
print()

print('Информация о 1-ом ревьювере')
print(reviewer_1)
print()

print('Информация о 2-ом ревьювере')
print(reviewer_2)
print()

student_list = [student_1, student_2]
lect_list = [lecturer_1, lecturer_2]
lect_list2 = [lecturer_2]


# средняя оценка по дз у всех студентов
def average_rating_all_s(course, student_list):
    sum_grade_all_s = 0
    len_grade_all_s = 0
    for std in student_list:
        if isinstance(std, Student) and course in std.courses_in_progress or course in std.finished_courses:
            sum_grade_all_s += std.average_rating_course_hw(course)[0]
            len_grade_all_s += std.average_rating_course_hw(course)[1]
        else:
            return f'{std.surname} {std.name} не изучает курс {course}'
            return 'Введены неверные данные'
    return round(sum_grade_all_s / len_grade_all_s, 1)


print('Средняя оценка за домашнии задания по всем студентам:')
print('Python:', average_rating_all_s('Python', student_list))
print('Git:', average_rating_all_s('Git', student_list))
print('Pycharm:', average_rating_all_s('Pycharm', student_list))
print()


# Средняя оценка за лекции всех лекторов
def average_rating_all_l(course, lecturer_list):
    sum_grade_all_l = 0
    len_grade_all_l = 0
    for lct in lecturer_list:
         if isinstance(lct, Lecturer) and course in lct.courses_attached:
             sum_grade_all_l += lct.average_rating_course_l(course)[0]
             len_grade_all_l += lct.average_rating_course_l(course)[1]
         else:
             return f'{lct.surname} {lct.name} не ведет лекции по курсу {course}'
             return 'Введены неверные данные'
    return round(sum_grade_all_l/len_grade_all_l, 1)


print('Средняя оценка за лекции всех лекторов в рамках курса:')
print('JS:', average_rating_all_l('JS', lect_list))
print('Git:', average_rating_all_l('Git', lect_list))
print('Python:', average_rating_all_l('Python', lect_list))
print()

print('сравнение студентов по средней оценке')
print('студент1 > студента2:', student_1 > student_2)
print('студент2 > студента1:', student_2 > student_1)
print('лектор1 > студента2:', lecturer_1 > student_2)
print()

print('сравнение лекторов по средней оценке')
print('лектор1 > лектора2:', lecturer_1 > lecturer_2)
print('лектор2 > лектора1:', lecturer_2 > lecturer_1)
print('лектор2 > студента1:', lecturer_2 > student_1)

