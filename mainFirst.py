def average(self):
    count = 0
    _sum = 0
    for grades in self.grades.values():
        count = count + 1
        _sum += sum(grades) / len(grades)
    self.average = round(_sum / count, 2)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = 0

    def student_rate(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f" Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.average}" \
               f" \nКурсы в процессе изучения: {self.courses_in_progress}" \
               f" \nЗавершенные курсы {self.finished_courses}"
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.average < other.average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average = 0
        self.courses_attached = []

    def __str__(self):
        text = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {self.average} "
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.average < other.average


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


def student_rating(student_list, course):
    sum = 0
    count = 0
    for student in student_list:
        if student.courses_in_progress == [course]:
            sum = sum + student.average
            count = count + 1
    average_all = sum / count
    return average_all


def lecturer_ratings(lecturer_list, course):
    sum = 0
    count = 0
    for lecturer in lecturer_list:
        if lecturer.courses_attached == [course]:
            sum = sum + lecturer.average
            count = count + 1
    average_all = sum / count
    return average_all


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

new_student.student_rate(new_cool_lecturer, 'IZO', 9)
new_student.student_rate(new_cool_lecturer, 'IZO', 5)

new_mentor = Reviewer('Павел', 'Антонов')
new_mentor.courses_attached += ['Python', 'IZO']

new_mentor.rate_hw(best_student, 'Python', 5)
new_mentor.rate_hw(best_student, 'Python', 10)
new_mentor.rate_hw(best_student, 'Python', 2)

new_mentor.rate_hw(new_student, 'IZO', 5)
new_mentor.rate_hw(new_student, 'IZO', 10)

average(Cool_Lecturer)
average(new_cool_lecturer)
average(best_student)
average(new_student)
average(new_student)
print(new_student)
print(best_student)
print(new_cool_lecturer)

print(Cool_Lecturer < new_cool_lecturer)
print(best_student > new_student)

student_list = [best_student, new_student]
lecturer_list = [Cool_Lecturer, new_cool_lecturer]


print(lecturer_ratings(lecturer_list, 'Python'))
print(student_rating(student_list, 'Python'))
