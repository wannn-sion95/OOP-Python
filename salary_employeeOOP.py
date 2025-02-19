print("-----------------------")
print("Salary of Employee")
print("-----------------------")
class employee:
    def __init__(self, name, id, department, salary):
        self.name = name
        self.id = id
        self.department = department
        self.salary = salary

    def display(self):
        return f"Nama: {self.name}\nID: {self.id}\nDepartment: {self.department}\nSalary: {self.salary}"

class human_resource(employee):
    def __init__(self, name, id, department, salary):
        super().__init__(name, id, department, salary)
        self.department = "Manager"

    def display(self):
        return f"Nama: {self.name}\nID: {self.id}\nDepartment: {self.department}\nSalary: {self.salary}"

emp = employee("Wannn Sion", 2224600080, "Konseling", "Rp.7.500.000")
emp2 = employee("Anita Helviana", 2224600081, "Asisten Konseling", "Rp.5.500.000")
hr = human_resource("Rayna Khairani", 3213458200, "HR", "Rp.11.500.000")
hrd = human_resource("Mhd. Ridwan", 3213458201, "HRD", "Rp.14.500.000")

print(emp.display())
print()
print(emp2.display())
print()
print(hr.display())
print()
print(hrd.display())
