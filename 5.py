#
class Employee:
    def calculate_salary(self):
        print("Employee salary")


class Developer(Employee):
    def calculate_salary(self):
        print("Developer salary: 50000")


class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary: 70000")


class Tester(Employee):
    def calculate_salary(self):
        print("Tester salary: 40000")


d = Developer()
m = Manager()
t = Tester()

d.calculate_salary()
m.calculate_salary()
t.calculate_salary()