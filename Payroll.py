class Payroll:
    def __init__(self,hours,hourly_payrate):
        self.hours = hours
        self.hourly_payrate = hourly_payrate
       
        self.regular_pay = 1.0
        self.overtime_pay = 2.0
        self.balanced_pay = 1.5
        
    def totalPay(self):
        self.total_pay = 0
        if self.hours <= 40 and self.hours != 0:
            self.total_pay = self.hours * self.regular_pay * self.hourly_payrate
            
        if self.hours <= 60 and self.hours > 40:
            self.pay = self.hours * self.balanced_pay * self.hourly_payrate
            self.overTime = self.overtimes()
            self.total_pay = self.overTime + self.pay
        
        if self.hours <= 80 and self.hours > 60:
            self.pay = self.hours * self.balanced_pay * self.hourly_payrate
            self.overTime = self.overtimes()
            self.total_pay = self.overTime + self.pay

        return self.total_pay
    
    def overtimes(self):
        if self.hours > 50:
            self.overtimepay = (self.hours - 50) * self.overtime_pay *  self.hourly_payrate
        else:
            self.overtimepay = 0

        return self.overtimepay
    
    def deductions(self):
        self.store_deductions= {}
        # Federal Withholding Rate
        self.federal_withholding = self.total_pay*(18/10)
        self.store_deductions['Federal Withholding'] = self.federal_withholding
        # State Withholding Rate
        self.State_withholding = self.total_pay*(4.5/10)
        self.store_deductions['State Withholding'] = self.State_withholding
        # Union_dues
        self.Union_dues = self.total_pay*(2/10)
        self.store_deductions['Union Dues'] = self.Union_dues

        return self.store_deductions

    def displayDeductions(self): 
        self.deduction_dict = self.deductions()
        for deduction, amount in self.deduction_dict.items():
            print("{} : {:.3f}".format(deduction,amount))

    def netpay(self):
        self.deduction_dict = self.deductions()
        self.totaldeductions = 0
        for i in self.deduction_dict.values():
            self.totaldeductions += i

        self.netPay = self.totalPay() - self.totaldeductions
        return self.netPay
    
employees = {}
def read_data():
    with open('employees.txt','r') as file:
        for line in file:
            employee_data = line.split()
            employee_name =employee_data[0]
            employees[employee_name] = {}
            employees[employee_name]['employee_worked_hours'] = sum(float(hour) for hour in employee_data[1:-1])
            employees[employee_name]['employee_hourly_rate'] = float(employee_data[-1])
        file.close()

def main():
   read_data()
   for employee_name,employee_data in employees.items():
        print(f'Employee Name : {employee_name}')
        print(f"Total worked hours : {employee_data['employee_worked_hours']}")
        print(f"Hourly Rate: {employee_data['employee_hourly_rate']}")
        payroll = Payroll(employee_data['employee_worked_hours'],employee_data['employee_hourly_rate'])
        print("Gross pay : {} ".format(payroll.totalPay()))
        payroll.deductions()
        payroll.displayDeductions()
        print("Net pay : {}".format(payroll.netpay()))
        print("-----------------------------------------")
main()

