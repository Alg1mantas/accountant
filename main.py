# sukurti programa, kuri ja paleidus priimtu du parametrus islaidai ir iplaukas eurais. 
# Ta programa turi paskaiciuoti: visu isplauku ir iplauku menesinius vidurkius 
# Turi paskaiciuoti dienos vidurkius
# Pajamu ir islaidu santyki procentaliai

# pajamu ketvircio rezultatus
# pusmecio islaidu rezultatus

import logging

logging.basicConfig(filename='accounting_logs.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')



class Accountant:

    def monthly_average(self, amount: float) -> float:
        logging.info(f"Receive amount of monthly average calculations:  {amount} ")
        return amount / 12

    def daily_average(self, amount: float) -> float:
        return amount / 365

    def calculate_ratio(self, income: float, expenses: float) -> float:
        return round(income / expenses, 2)



class Income(Accountant):
    def __init__(self, income: float):
        self.income = income
    
    def quarter_income(self) -> float:
        return self.income / 4


class Expenses(Accountant):
    def __init__(self, expenses: float):
        self.expenses = expenses
    
    
    def half_year_expenses(self) -> float:
        return self.expenses / 2



def main() -> None:
    income = float(input("Enter your yearly income: "))
    expenses = float(input("Enter your yearly expenses: "))
    logging.info(f"log income amount {income} ")
    logging.info(f"log expenses amount {expenses} ")
    inc = Income(income)
    exp = Expenses(expenses)
    print(f"quarter income is : {inc.quarter_income()}")
    print(f"daily average is : {exp.daily_average(expenses)}")
    
    

if __name__=='__main__':
    main()





    

