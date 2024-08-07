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
