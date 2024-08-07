import pprint


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lr(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def avr_grade(self):
        if not self.grades:
            return 0
        total_sum = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return round(total_sum / total_count, 2)

    def __str__(self):
        return (
            f"Имя: {self.name} \n"
            f"Фамилия: {self.surname} \n"
            f"Средняя оценка за домашние задания: {self.avr_grade()} \n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)} \n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )

    def __lt__(self, other):
        return self.avr_grade() < other.avr_grade()

    def __le__(self, other):
        return self.avr_grade() <= other.avr_grade()

    def __gt__(self, other):
        return self.avr_grade() > other.avr_grade()

    def __ge__(self, other):
        return self.avr_grade() >= other.avr_grade()

    def __eq__(self, other):
        return self.avr_grade() == other.avr_grade()

    def __ne__(self, other):
        return self.avr_grade() != other.avr_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avr_grade(self):
        if not self.grades:
            return 0
        total_sum = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return round(total_sum / total_count, 2)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avr_grade()}"

    def __lt__(self, other):
        return self.avr_grade() < other.avr_grade()

    def __le__(self, other):
        return self.avr_grade() <= other.avr_grade()

    def __gt__(self, other):
        return self.avr_grade() > other.avr_grade()

    def __ge__(self, other):
        return self.avr_grade() >= other.avr_grade()

    def __eq__(self, other):
        return self.avr_grade() == other.avr_grade()

    def __ne__(self, other):
        return self.avr_grade() != other.avr_grade()


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
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


student1 = Student("Кирил", "Хугардиан", "М")
student2 = Student("Мария", "Соколова", "Ж")

lecturer1 = Lecturer("Иван", "НаНаНаНиев")
lecturer2 = Lecturer("Андрей", "Скайуокер")

reviewer1 = Reviewer("Елена", "Сидорова")
reviewer2 = Reviewer("Контантин", "Соловьев")


student1.courses_in_progress += ["Python", "Sql"]
student2.courses_in_progress += ["Python", "Sql"]

student1.finished_courses += ["Введение в программирование"]
student2.finished_courses += ["Введение в программирование"]

lecturer1.courses_attached += ["Python"]
lecturer2.courses_attached += ["Sql"]

reviewer1.courses_attached += ["Python"]
reviewer2.courses_attached += ["Sql"]


reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student1, "Python", 8)
reviewer1.rate_hw(student1, "Sql", 6)
reviewer1.rate_hw(student1, "Sql", 7)

reviewer2.rate_hw(student2, "Python", 3)
reviewer2.rate_hw(student2, "Python", 5)
reviewer2.rate_hw(student2, "Sql", 9)
reviewer2.rate_hw(student2, "Sql", 9)

# Оценки за лекции
student1.rate_lr(lecturer1, "Python", 9)
student1.rate_lr(lecturer1, "Python", 10)

student2.rate_lr(lecturer2, "Sql", 8)
student2.rate_lr(lecturer2, "Sql", 7)

print(student1)
print(student2)

print(lecturer1)
print(lecturer2)

print(reviewer1)
print(reviewer2)

print(student1 < student2)
print(lecturer1 > lecturer2)


def avr_grades_students(students, course):
    total_sum = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_sum += sum(student.grades[course])
            total_count += len(student.grades[course])
    if total_count == 0:
        return 0
    return round(total_sum / total_count, 2)


def avr_grades_lectures(lecturers, course):
    """Подсчет средней оценки за лекции всех лекторов в рамках курса"""
    total_sum = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_sum += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    if total_count == 0:
        return 0
    return round(total_sum / total_count, 2)


students = [student1, student2]
lecturers = [lecturer1, lecturer2]
course = "Python"

print("Средняя оценка студентов по курсу", course, ":", avr_grades_students(students, course))
print("Средняя оценка лекторов по курсу", course, ":", avr_grades_lectures(lecturers, course))
