# def aver(self):
#     count = 0
#     _sum = 0
#     gr = []
#     for grades in self.grades.values():
#         count = count + 1
#         gr = grades
#         print(gr)
#         _sum = _sum + grades
#         print(grades)
#         print(count)
#     self.avarage = _sum / count
#     print(self.avarage)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avarage = 0

    def student_rate(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.lec_grades:
                lector.lec_grades[course] += [grade]
            else:
                lector.lec_grades[course] = [grade]
        else:
             return 'Ошибка'




    def __str__(self):
        text = f" Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.avarage}" \
               f" \nКурсы в процессе изучения: {self.courses_in_progress}" \
               f" \nЗавершенные курсы {self.finished_courses}"
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.grades < other.grades


class Mentor:
     def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lec_grades = {}

    # def average_lec_rating(self, lector, course):
    #     if isinstance(lector, Lecturer):
    #         for cource in self.courses_attached:
    #             print(cource)
    #             pass

    def __str__(self):
        text = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {  self.lec_grades.values()} "
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.lec_grades < other.lec_grades

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
        text = f"Имя: {self.name} \nФамилия: {self.surname}"
        return text

best_student = Student('Alex', 'Drugov', 'men')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Прыжки в длину']

new_student = Student('Oleg', 'Privetov', 'men')
new_student.courses_in_progress += ['IZO']



Cool_Lecturer = Lecturer('Some', 'Buddy')
Cool_Lecturer.courses_attached += ['Python']

best_student.student_rate(Cool_Lecturer, 'Python', 10)
best_student.student_rate(Cool_Lecturer, 'Python', 9)
best_student.student_rate(Cool_Lecturer, 'Python', 8)

new_cool_lecturer = Lecturer('Valera', 'Pupkin')
new_cool_lecturer.courses_attached += ['IZO']

new_cool_lecturer.average_lec_rating()

new_student.student_rate(new_cool_lecturer, 'IZO', 9)
new_student.student_rate(new_cool_lecturer, 'IZO', 5)

print(new_cool_lecturer)


new_mentor = Reviewer('Павел', 'Антонов')
new_mentor.courses_attached += ['Python']

new_mentor.rate_hw(best_student, 'Python', 5)
new_mentor.rate_hw(best_student, 'Python', 10)
new_mentor.rate_hw(best_student, 'Python', 2)




print(best_student)


