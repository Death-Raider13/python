class Company:
    def __init__(self, company_name, company_age, company_perferences,):
        self.name = company_name
        self.age = company_age
        self.perferences = company_perferences

  

class Employee(Company):
    def __init__(self, name, idnumber, salary, post, company_name, company_age, company_perferences):
        Company.__init__(self, company_name, company_age, company_perferences)
        self.name = name
        self.idnumber = idnumber
        self.salary = salary
        self.post = post

    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)

a = Employee ('Penguin', 20210401, 15000, "Intern", "TechCorp", 5, "Innovative")
a.display()
