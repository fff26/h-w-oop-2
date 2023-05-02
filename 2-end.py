class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        try:
            average_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}"
        except ZeroDivisionError:
            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: 0"
        
    def av_grade_course_lectors(course):
        grade_list = []
        for key, value in super().grades():
            if key == course:
                grade_list.append(value)
        return f'Средняя оценка всех лекторов в рамках курса {course}: {round(sum(grade_list)/len(grade_list), 1)}'
    
    def __lt__(self, other):
        """
        Этот метод определяет оператор "меньше чем" (__lt__) для двух лекторов.
        Он сравнивает среднее значение оценок обоих объектов и возвращает булево значение.
        Если ни один из объектов не имеет оценок, возвращается строка с именем и фамилией обоих лекторов.
        """
        try:
            return sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])) < sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), []))
        except ZeroDivisionError:
            return f'{self.name} {self.surname} и/или {other.name} {other.surname} не имеют оценок для сравнения.'

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
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        try:
            average_grade = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"
        except ZeroDivisionError:
            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: 0\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"
    
    def __lt__(self, other):
        """
        Этот метод определяет оператор "меньше чем" (__lt__) для двух объектов.
        Он сравнивает среднее значение оценок обоих студентов и возвращает булево значение.
        Если ни один из объектов не имеет оценок, возвращается строка с именами студентов.
        """
        try:
            return sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])) < sum(sum(other.grades.values(), [])) / len(sum(other.grades.values(), []))
        except ZeroDivisionError:
            return f'{self.name} {self.surname} и/или {other.name} {other.surname} не имеют оценок для сравнения.'
        
    def av_grade_course_lectors(course):
        grade_list = []
        for key, value in Student.grades():
            if key == course:
                grade_list.append(value)
        return f'Средняя оценка всех студентов в рамках курса {course}: {round(sum(grade_list)/len(grade_list), 1)}'
                    
lecturer_1 = Lecturer('Владимир', 'Путин')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Владимир', 'Зеленский')
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Алексей', 'Резников')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Сергей', 'Шойгу')
reviewer_2.courses_attached += ['Git']

student_1 = Student('Джо', 'Байден', 'male')
student_1.finished_courses += ['Git']
student_1.courses_in_progress += ['Python']
student_2 = Student('Ллойд', 'Остин', 'male')
student_2.finished_courses += ['Python']
student_2.courses_in_progress += ['Git']

print(lecturer_1.__str__())
reviewer_1.rate_hw(student_1, 'Python', 5)
print(lecturer_1 > lecturer_2)
print(student_1 > student_2)