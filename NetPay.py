import PayrollDeductionClass as p
import EmployeeClass as e


def main():

    employee1 = e.employee('Jimmy Smith', '58475','Information Systems','developer','6800.00')

    foodCourt1 = p.payrollDeduction('food court', '8/14/2022', '22.50', '39119')
    giftContribution = p.payrollDeduction('gift contribution', '8/12/2022', '25.00', '58475')
    foodCourt2 = p.payrollDeduction('food court', '8/17/2022', '15.25', '21547')
    vendingMachine1 = p.payrollDeduction('vendingMachine', '8/22/2022', '3.00', '58475')
    vendingMachine2 = p.payrollDeduction('vendingMachine', '8/5/2022', '2.75', '58475')


    netPay = float(employee1.getMonthlySalary()) - float(vendingMachine1.getChargeAmount()) - float(vendingMachine2.getChargeAmount()) - float(giftContribution.getChargeAmount())


    print('*** Employee Pay ***')
    print('Name: ' + employee1.getName())
    print('ID Number: ' + employee1.getIdNum())
    print('Department: ' + employee1.getDepartment())
    print('Gross Pay: ' + employee1.getMonthlySalary())
    print('Net Pay: ' + str(netPay))





main()