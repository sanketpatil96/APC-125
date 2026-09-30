# 1
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def annual_salary(self):
        return self.salary * 12

    def display(self):
        super().display()
        print("Department:", self.department)
        print("Annual Salary:", self.annual_salary())


e = Employee(101, "Rahul", 30000)
m = Manager(102, "Amit", 50000, "Sales")

e.display()
print()
m.display()


# 2
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self):
        super().display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)
        print("Price after discount:", self.discounted_price(10))


car = Car("Toyota", "Fortuner", "Diesel", 3000000)
car.display()


# 3
class Academic:
    def __init__(self, marks):
        self.marks = marks

    def academic_score(self):
        return sum(self.marks) / len(self.marks)


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points

    def sports_score(self):
        return self.sports_points


class Student(Academic, Sports):
    def __init__(self, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)

    def overall_performance(self):
        return (self.academic_score() + self.sports_score()) / 2


s = Student([80, 85, 90], 85)

print("Academic Score:", s.academic_score())
print("Sports Points:", s.sports_score())
print("Overall Performance:", s.overall_performance())


# 4
class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


e = Employee("Rahul", 25, 101, "Developer", 50000)
e.display()


# 5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


r = ResearchStudent(
    "Amit", 24, 101, "M.Sc",
    "Artificial Intelligence", "Dr. Sharma"
)

r.display()


# 6
class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        super().display()
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)


account = PremiumSavingsAccount(
    12345, 100000, 6, "Free ATM and Insurance"
)

account.display()


# 7
import math

class Shape:
    def display_name(self):
        print("Shape:", self.__class__.__name__)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = Circle(7)
r = Rectangle(10, 5)
t = Triangle(10, 6)

c.display_name()
print("Area:", c.area())

r.display_name()
print("Area:", r.area())

t.display_name()
print("Area:", t.area())


# 8
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)


class Manager(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.30


class Developer(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.20


class Tester(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.15


m = Manager(101, "Rahul", 50000)
d = Developer(102, "Amit", 40000)
t = Tester(103, "Priya", 35000)

m.display()
print("Manager Salary:", m.salary())
print()

d.display()
print("Developer Salary:", d.salary())
print()

t.display()
print("Tester Salary:", t.salary())


# 9
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def student_details(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)


class Faculty(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def faculty_details(self):
        print("Faculty Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, subject):
        Student.__init__(self, name, age, roll_no)
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)


ta = TeachingAssistant("Rahul", 22, 101, "Python")
ta.display()


# 10
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def car_details(self):
        print("Car Model:", self.model)


class Bike(Vehicle):
    def __init__(self, brand, engine):
        super().__init__(brand)
        self.engine = engine

    def bike_details(self):
        print("Engine:", self.engine)


class SportsCar(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

    def display(self):
        super().display()
        self.car_details()
        print("Top Speed:", self.top_speed)


class ElectricBike(Bike):
    def __init__(self, brand, engine, battery):
        super().__init__(brand, engine)
        self.battery = battery

    def display(self):
        super().display()
        self.bike_details()
        print("Battery:", self.battery)


sc = SportsCar("Ferrari", "F8", "340 km/h")
eb = ElectricBike("Ola", "Electric", "5 kWh")

sc.display()
print()

eb.display()


# 11
class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 3

    def grade(self):
        p = self.percentage()

        if p >= 90:
            return "A+"
        elif p >= 80:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Total:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())


r = Result(101, "Rahul", "BCA", [85, 90, 80])
r.display()


# 12
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
        print("Final Price:", self.final_price(10))


p = ElectronicProduct(
    101, "Laptop", 60000, "HP", "2 Years"
)

p.display()


# 13
class Printer:
    def print_document(self):
        print("Printing document...")


class Scanner:
    def scan_document(self):
        print("Scanning document...")


class MultifunctionDevice(Printer, Scanner):
    def display(self):
        self.print_document()
        self.scan_document()


device = MultifunctionDevice()
device.display()


# 14
class Camera:
    def take_photo(self):
        print("Photo taken")


class Phone:
    def make_call(self, number):
        print("Calling", number)


class Smartphone(Camera, Phone):
    def display(self):
        self.take_photo()
        self.make_call("9876543210")


phone = Smartphone()
phone.display()


# 15
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


r = ResearchStudent(
    "Priya", 25, 102, "MCA",
    "Machine Learning", "Dr. Kumar"
)

r.display()


# 16
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


r = ResearchStudent(
    "Amit", 24, 103, "M.Sc",
    "Data Science", "Dr. Sharma"
)

r.display()


# 17
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def sound(self):
        print(self.name, "says Woof")


class Cat(Animal):
    def sound(self):
        print(self.name, "says Meow")


class Cow(Animal):
    def sound(self):
        print(self.name, "says Moo")


dog = Dog("Tommy")
cat = Cat("Kitty")
cow = Cow("Gauri")

dog.eat()
dog.sound()

cat.eat()
cat.sound()

cow.eat()
cow.sound()


# 18
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def doctor_details(self):
        print("Doctor:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def patient_details(self):
        print("Patient:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)


class Surgeon(Doctor, Patient):
    def __init__(self, name, age, specialization, disease):
        Doctor.__init__(self, name, age, specialization)
        self.disease = disease

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Disease:", self.disease)


class MedicalResearcher(Doctor):
    def __init__(self, name, age, specialization, research_area):
        super().__init__(name, age, specialization)
        self.research_area = research_area

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Research Area:", self.research_area)


doctor = Doctor("Dr. Rahul", 40, "Cardiology")
patient = Patient("Amit", 30, "Heart Disease")
surgeon = Surgeon("Dr. Priya", 45, "General Surgery", "Appendicitis")
researcher = MedicalResearcher(
    "Dr. Sharma", 50, "Neurology", "Brain Research"
)

doctor.doctor_details()
print()

patient.patient_details()
print()

surgeon.display()
print()

researcher.display()
