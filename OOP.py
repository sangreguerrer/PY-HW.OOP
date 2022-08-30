mentor_list = []
student_list = []
class Student:
    def __init__(self,name,surname,gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}
        student_list.append(self)
        
    def __str__(self):
        info = f"Имя: {self.name},\nФамилия: {self.surname}\nСредняя оценка за домашние задания:\n{self.average()} \nКурс:{self.__progress()},\nЗавершённые курсы: {self.__finished()}."
        return info
    

    def __progress(self):
        courses_in_progress = ','.join(self.courses_in_progress)
        return courses_in_progress
    
    
    def __finished(self):
        finished_courses = ','.join(self.finished_courses)
        return finished_courses
    
    
    
    def average(self):
        count=0
        for counter in self.grades:
            count+=1
        for value in self.grades.values():
            for v in value:
                avg = sum(map(sum,self.grades.values()))/count
                return avg
                           

    def rate_lecs(self,lecturer,course,grade):
            if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
                    
                    
    def __eq__(self,other):
        return self.average() == other.average()
    
    def __it__(self,other):
        return self.average() < other.average()
    
    def __gt__(self,other):
        return self.average() > other.average()

            
            
class Mentor:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__(self,name,surname):
        self.grades = {}
        super().__init__(name,surname)
        mentor_list.append(self)
        
    def average(self):
        count=0
        for counter in self.grades:
            count+=1
        for value in self.grades.values():
            for v in value:
                avg = sum(map(sum,self.grades.values()))/count
                return avg
            
           
            
            
    def __eq__(self,other):
        return self.average() == other.average()
    
    def __it__(self,other):
        return self.average() < other.average()
    
    def __gt__(self,other):
        return self.average() > other.average()
                       
    def __str__(self):
            return f"Имя:{self.name},\nФамилия: {self.surname},\nСредняя оценка за лекции: {self.average(mentor_list,'Python')}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
        
    def rate_hw(self,student,course,grade):
        if isinstance(student,Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        info_rev = f"Имя: {some_reviewer.name},\nФамилия: {some_reviewer.surname}"
        return info_rev
    

def course_average(roster,course):
    count_grades = 0
    sum_grades = 0
    for person in roster:
        for key,values in person.grades.items():
            if course in key:
                for v in values:
                    count_grades+=1
                    sum_grades+=v
                    avg = sum_grades/count_grades
                    return avg   

    
some_lecturer = Lecturer("Some","Buddy")
some_lecturer.courses_attached += ['Python']


some_student = Student('Rouy','Eman','male',)



some_student.courses_in_progress += ['Python','Git']
some_student.finished_courses.append('Введение в программирование')
some_reviewer = Reviewer('Some','Buddy')

lecturer1 = Lecturer("Иосиф","Москвин")
lecturer1.courses_attached += ['Python','Git']


lecturer2 = Lecturer("Сергей","Палыч")
lecturer2.courses_attached += ['Python','Git']



student1 = Student("Валерий","Покрышкин","male")
student1.courses_in_progress += ['Python' , 'Git']
student1.finished_courses = ['Java']

student2 = Student("Максим","Каргапов","male")
student2.courses_in_progress += ['Python' , 'Jango']
student2.finished_courses = ["CSharp"]

angry_reviewer = Reviewer("Вадим","Марков")
angry_reviewer.courses_attached = ['Python','Git']




angry_reviewer.rate_hw(student1,'Python',8)
angry_reviewer.rate_hw(student1,'Git',2)
angry_reviewer.rate_hw(student2,'Python',7)
angry_reviewer.rate_hw(student2,'Git',5)
angry_reviewer.rate_hw(some_student,'Python',6)

student1.average
student2.average
some_student.average




student1.rate_lecs(lecturer2,'Python',6)
student1.rate_lecs(lecturer1,'Python',9)
student1.rate_lecs(some_lecturer,'Python',5)
student1.rate_lecs(lecturer2,'Git',9)
student1.rate_lecs(lecturer1,'Git',4)
student1.rate_lecs(some_lecturer,'Git',5)

lecturer2.average
lecturer1.average
some_lecturer.average

print(lecturer2 < lecturer1)
print(student1 > student2)

print(course_average(student_list,'Python'))
print(course_average(mentor_list,'Python'))
print(course_average(mentor_list,'Git'))

print(student1.grades)
