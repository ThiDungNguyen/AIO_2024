from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self.__name = name
        self.__yob = yob

    def get_yob(self):
        return self.__yob

    def set_yob(self, yob):
        self.__yob = yob

    # __: private, chỉ dùng được ở trong cùng 1 class, muốn sử dụng thay đổi biến private thì cần dùng các hàm đặc biệt như: get_name, set_name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade: str):
        super().__init__(name=name, yob=yob)
        self.__grade = grade

    def describe(self):
        print(f'name: {self.get_name()}, yob: {
              self.get_yob()}, grade: {self.__grade}')


class Teacher(Person):
    def __init__(self, name, yob, subject: str):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(f'name: {self.get_name()}, yob: {
              self.get_yob()}, grade: {self.__subject}')


class Doctor(Person):
    def __init__(self, name, yob, specialist: str):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(f'name: {self.get_name()}, yob: {
              self.get_yob()}, grade: {self.__specialist}')


class Ward:
    def __init__(self, name: str):
        # super().__init__(name)
        self.__name = name
        self.__list_people = list()

    def add_person(self, person: Person):
        self.__list_people.append(person)

    def describe(self):
        print(f" Ward Name : {self.__name}")
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        counter = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):  # if type(person) == Doctor
                counter += 1
        return counter

    def sort_yob(self):
        return self.__list_people.sort(key=lambda x: x.get_yob())

    def comput_average(self):
        sum_age = 0
        sum_age_teacher = 0
        count_teacher = 0
        for p in self.__list_people:
            if isinstance(p, Teacher):
                count_teacher += 1
                sum_age_teacher += p.get_yob()
            sum_age += p.get_yob()
        ave = sum_age/len(self.__list_people)
        ave_teacher = sum_age_teacher / count_teacher
        print(f'ave: {ave}, ave_teacher: {ave_teacher}')
        return ave, ave_teacher


# q5
student1 = Student("studentZ2023", 2011, "6")
assert student1.get_yob() == 2011
student1.describe()

# q6
teacher1 = Teacher("teacherZ2023", 1991, " History ")
assert teacher1.get_yob() == 1991
teacher1.describe()

# q7
doctor1 = Doctor("doctorZ2023", 1981, " Endocrinologists ")
assert doctor1.get_yob() == 1981
doctor1.describe()

# q8
student1 = Student(" studentA ", 2010, "7")
teacher1 = Teacher(" teacherA ", 2009, " Math ")
teacher2 = Teacher(" teacherB ", 1978, " History ")
doctor1 = Doctor(" doctorA ", 1945, " Endocrinologists ")
print('done')
ward1 = Ward(name="Ward1")
print(ward1.describe())
assert ward1.count_doctor() == 0
doctor2 = Doctor("doctorB ", 1975, " Cardiologists ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.count_doctor()
print(ward1.describe())
ward1.comput_average()
