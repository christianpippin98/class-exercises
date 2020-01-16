import datetime

class Employee:
    def __init__(self, name, job_title):
        self.full_name = name
        self.job_title = job_title
        self.hire_date = ""

class Company:
    def __init__(self, name, address, industry):
        self.business_name = name
        self.address = address
        self.industry_type = industry
        self.employees = list()

    def hire_employee(self, Employee):
        Employee.hire_date = datetime.datetime.now()
        self.employees.append(Employee)

    def list_employees(self):
        employee_list = ""
        for person in self.employees:
            employee_list += f"\n{person.full_name} "
        print(f"{self.business_name} is a {self.industry_type} company and employs the following people; {employee_list}")

christian = Employee("Christian Pippin", "Software Engineer")
corri = Employee("Corri Golden", "Software Developer")
lauren = Employee("Lauren Riddle", "Full-Stack Engineer")
matt = Employee("Matt Blagg", "Front-End Developer")
jeremiah = Employee("Jeremiah Bell", "Back-End Engineer")

amazon = Company("Amazon", "100 Silicon Dr", "E-Commerce")
google = Company("Google", "200 Silicon Dr", "Tech")

amazon.hire_employee(corri)
google.hire_employee(lauren)
amazon.hire_employee(matt)
google.hire_employee(jeremiah)
amazon.hire_employee(christian)

amazon.list_employees()
google.list_employees()