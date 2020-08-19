class Employee():
    Regsalary=2000
    TempSalary=300
    def __init__(self,empid,name,age,position):
        self.empid=empid
        self.name=name
        self.age=age
        self.position=position
        
        
class RegularEmp(Employee):
    def wageCalc(self,daysworked):
        total_salary=daysworked*Employee.Regsalary
        print(total_salary)


class TempEmployee(Employee):
    def wageCalc(self,hoursworked):
        total_salary=hoursworked*Employee.TempSalary
        print(total_salary)


regemp1=RegularEmp(101,'Monica',27,'SoftwareEngineer')
regemp1.wageCalc(20)
tempEmp1=TempEmployee(102,'Preethi',23,'SoftwareEngineer')
tempEmp1.wageCalc(70)
    
        
    
