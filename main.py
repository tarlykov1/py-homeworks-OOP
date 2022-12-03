class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rategrade(self):
        if not self.grades:
            return 0
        list=[] 
        for k in self.grades.values():
             list.extend(k)
        return round(sum(list)/len(list), 2)
        
    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.rategrade()}\n' \
              f'Курсы в процессе обучени: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res
      
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
           if course in lecturer.grades:
               lecturer.grades[course] += [grade]
           else:
               lecturer.grades[course] = [grade]
        else:
            return'Ошибка'
          
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нельзя сравнивать')
            return  
        return self.rategrade() < other.rategrade()
      
    def __le__(self, other):
        if not isinstance(other, Student):
            print('Нельзя сравнивать')
            return  
        return self.rategrade() > other.rategrade()
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Нельзя сравнивать')
            return  
        return self.rategrade() == other.rategrade()
      
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
      
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
              
    def rategrade(self):
        if not self.grades:
            return 0
        spisok=[]
        for k in self.grades.values():
           spisok.extend(k)
        return round(sum(spisok)/len(spisok), 2)
        
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.rategrade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нельзя сравнивать')
            return
        return self.rategrade() < other.rategrade()

    def __eq__(self,other):
        if not isinstance(other, Lecturer):
            print('Нельзя сравнивать')
            return
        return self.rategrade == other.rategrade
      
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else: 
                student.grades[course] = [grade]
        else:
            return'Ошибка'
          
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
      
best_lecturer_1 = Lecturer('Олег', 'Булыгин')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Дмитрий', 'Федин')
best_lecturer_2.courses_attached += ['Java']

best_lecturer_3 = Lecturer('Елена', 'Никитина')
best_lecturer_3.courses_attached += ['Python']
    
cool_rewiewer_1 = Reviewer('Александр', 'Бардин')
cool_rewiewer_1.courses_attached += ['Python']
cool_rewiewer_1.courses_attached += ['Java']

cool_rewiewer_2 = Reviewer('Игорь', 'Сверчков')
cool_rewiewer_2.courses_attached += ['Python']
cool_rewiewer_2.courses_attached += ['Java']

student_1 = Student('Дмитрий', 'Тарлыков')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Python-разработчик с нуля']

student_2 = Student('Даниил', 'Петров')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Java-разработчик с нуля']

student_3 = Student('Олег', 'Нагорный')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Python-разработчик с нуля']

student_1.rate_hw(best_lecturer_1, 'Python', 3)
student_1.rate_hw(best_lecturer_1, 'Python', 2)
student_1.rate_hw(best_lecturer_1, 'Python', 4)

student_1.rate_hw(best_lecturer_2, 'Java', 1)
student_1.rate_hw(best_lecturer_2, 'Java', 4)
student_1.rate_hw(best_lecturer_2, 'Java', 10) 

student_1.rate_hw(best_lecturer_1, 'Python', 2)
student_1.rate_hw(best_lecturer_1, 'Python', 5)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_2.rate_hw(best_lecturer_2, 'Java', 1)
student_2.rate_hw(best_lecturer_2, 'Java', 10)
student_2.rate_hw(best_lecturer_2, 'Java', 7)

student_3.rate_hw(best_lecturer_3, 'Python', 3)
student_3.rate_hw(best_lecturer_3, 'Python', 9)
student_3.rate_hw(best_lecturer_3, 'Python', 6)

cool_rewiewer_1.rate_hw(student_1, 'Python', 4)
cool_rewiewer_1.rate_hw(student_1, 'Python', 2)
cool_rewiewer_1.rate_hw(student_1, 'Python', 8)

cool_rewiewer_2.rate_hw(student_2, 'Java', 1)
cool_rewiewer_2.rate_hw(student_2, 'Java', 10)
cool_rewiewer_2.rate_hw(student_2, 'Java', 5)

cool_rewiewer_2.rate_hw(student_3, 'Python', 6)
cool_rewiewer_2.rate_hw(student_3, 'Python', 4)
cool_rewiewer_2.rate_hw(student_3, 'Python', 10)
cool_rewiewer_2.rate_hw(student_3, 'Python', 5)
cool_rewiewer_2.rate_hw(student_3, 'Python', 2)
cool_rewiewer_2.rate_hw(student_3, 'Python', 6)

print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()


student_list = [student_1 , student_2, student_3]
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

def student_rating(student_list, course_name):
    count_all = []
    for stud in student_list:
        count_all.extend(stud.grades.get(course_name,[]))
    if not count_all:
        return 'По такому курсу нет оценок'
    return round(sum(count_all)/len(count_all),2)
    
def lecturer_rating(lecturer_list, course_name):
    count_all = []
    for lectur in lecturer_list:
        count_all.extend(lectur.grades.get(course_name,[]))
    if not count_all:
        return 'По такому курсу нет оценок'
    return round(sum(count_all)/len(count_all),2)
    
print(f"Средняя оценка для всех студентов по курсу {'Java'}: {student_rating(student_list, 'Java')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()    