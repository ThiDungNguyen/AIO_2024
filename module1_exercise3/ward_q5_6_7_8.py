from abc import ABC, abstractmethod


class Person (ABC):
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    def get_yob(self):
        return self.yob

    @abstractmethod
    def describe(self):
        pass


class Student (Person):
    def __init__(self, name: str, yob: int, grade: str):
        # Your Code Here
        self.name = name
        self.yob = yob
        self.grade = grade

    # End Code Here

    def describe(self):
        # Your Code Here
        print(f'name: {self.name}, yob: {self. yob}, grade: {self.grade}')
        # End Code Here


class Teacher (Person):
    def __init__(self, name: str, yob: int, subject: str):
        # Your Code Here
        self.name = name
        self.yob = yob
        self.subject = subject

        # End Code Here

    def describe(self):
        # Your Code Here
        print(f'name: {self.name}, yob: {self. yob}, grade: {self.subject}')
        # End Code Here


class Doctor (Person):
    def __init__(self, name: str, yob: int, specialist: str):
        # Your Code Here
        self.name = name
        self.yob = yob
        self.specialist = specialist
        # End Code Here

    def describe(self):
        # Your Code Here
        print(f'name: {self.name}, yob: {self. yob}, grade: {self.specialist}')
        # End Code Here


class Ward:
    def __init__(self, name: str):
        self.name = name
        self.listPeople = list()

    def add_person(self, person: Person):
        self.listPeople . append(person)

    def describe(self):
        print(f" Ward Name : {self.name}")
        for p in self.listPeople:
            p.describe()

    def count_doctor(self):
        count = sum(1 for p in self.listPeople if isinstance(p, Doctor))
        print('Number of doctors:', count)
        return count
        

'''# q5
# student1 = Student ( name =" studentZ2023 ", yob =2011 , grade ="6")
# assert student1.yob == 2011
# student1.describe ()
# q6
# teacher1 = Teacher ( name =" teacherZ2023 ", yob =1991 , subject =" History ")
# assert teacher1.yob == 1991
# teacher1 . describe ()
# q7
# doctor1 = Doctor(name=" doctorZ2023 ", yob=1981,
#                 specialist=" Endocrinologists ")
# assert doctor1 . yob == 1981
# doctor1 . describe()
'''     
# q8


student1 = Student(name=" studentA ", yob=2010, grade="7")
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
ward1 = Ward(name=" Ward1 ")
assert ward1.count_doctor() == 1
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 . add_person(student1)
ward1 . add_person(teacher1)
ward1 . add_person(teacher2)
ward1 . add_person(doctor1)
ward1 . add_person(doctor2)
ward1 . count_doctor()
