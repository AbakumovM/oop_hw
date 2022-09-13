class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __average_output(self):
        sum_grade, amount_grade = 0, 0
        for grade in self.grades.values():
            for i in grade:
                amount_grade += 1
                sum_grade += i
        return round(sum_grade / amount_grade, 2)


    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.__average_output() < other.__average_output()     


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average_output()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}  '
        return res     


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __average_output(self):
        sum_grade, amount_grade = 0, 0
        for grade in self.grades.values():
            for i in grade:
                amount_grade += 1
                sum_grade += i
        return round(sum_grade / amount_grade, 2) 

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print('Not a Lecturer!')
            return
        return self.__average_output() < other.__average_output()     


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_output()} '
        return res    


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname} '
        return res

# создаем первого студента 
best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
# создлаем второго студента
best_student_2 = Student('Jon', 'Jones', 'man')
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Git']
best_student_2.finished_courses += ['C++', 'Введение в программирование']


# создаем первого проверяющего
reviewer_1 = Reviewer('Tom', 'Ford')
reviewer_1.courses_attached += ['Python']
# создаем второго проверяющего
reviewer_2 = Reviewer('Alan', 'Wake')
reviewer_2.courses_attached += ['Python']


# первый проверяющий выставляет оценки первому студенту и второму
reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student, 'Python', 9)
reviewer_1.rate_hw(best_student, 'Python', 5)
reviewer_1.rate_hw(best_student_2, 'Python', 9)
reviewer_1.rate_hw(best_student_2, 'Python', 7)
reviewer_1.rate_hw(best_student_2, 'Python', 7)
# второй проверяющий выставляет оценки первому студенту и второму
reviewer_2.rate_hw(best_student_2, 'Python', 8)
reviewer_2.rate_hw(best_student_2, 'Python', 10)
reviewer_2.rate_hw(best_student_2, 'Python', 7)
reviewer_2.rate_hw(best_student, 'Python', 9)
reviewer_2.rate_hw(best_student, 'Python', 6)
reviewer_2.rate_hw(best_student, 'Python', 8)


# создаем первого лектора
lect_1 = Lecturer('Mark', 'Bolt')
lect_1.courses_attached += ['Python']
# создаем второго лектора
lect_2 = Lecturer('Max', 'Moral')
lect_2.courses_attached += ['Python']


# первый студент выставляет оценки первому лектору
best_student.rate_lecture(lect_1, 'Python', 10)
best_student.rate_lecture(lect_1, 'Python', 10)
best_student.rate_lecture(lect_1, 'Python', 10)
best_student.rate_lecture(lect_1, 'Python', 4)
# второй студент выставляет оценки второму лектору
best_student_2.rate_lecture(lect_2, 'Python', 10)
best_student_2.rate_lecture(lect_2, 'Python', 9)
best_student_2.rate_lecture(lect_2, 'Python', 8)
best_student_2.rate_lecture(lect_2, 'Python', 6)


student_list = [best_student, best_student_2]
lector_list = [lect_1, lect_2]

# считает среднее значение оценки за домашние задания по всем студентам в рамках конкретного курса
def average_student(student, courses):
    count_student = 0
    sum_grades = 0  
    for i in student:
            for k in i.grades:
                if courses in k:
                    count_student += 1
                    sum_grades += sum(i.grades[k]) / len(i.grades[k])
    if  count_student > 0:
        return f'Средняя оценка всех студентов курса {courses}: {round(sum_grades / count_student, 3)}'
    else:
        return f'Студенты не получали оценки по курсу {courses}'    

# считает среднее значение оценки за лекции всех лекторов в рамках курса
def average_lect(lector, courses):
    count_lector = 0
    sum_grades = 0  
    for i in lector:
        for k in i.grades:
            if courses in k:
                count_lector += 1
                sum_grades += sum(i.grades[k]) / len(i.grades[k])
    if count_lector > 0:
        return f'Средняя оценка всех лекторов по курсу {courses}: {round(sum_grades / count_lector, 3)}'
    else:
        return f'лекторы не получали оценки по курсу {courses}'               

print(average_lect(lector_list, 'Python'))