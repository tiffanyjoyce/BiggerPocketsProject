class ROICalculator():

    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cashflow = 0
        self.ROIperc = 0
    def TotalIncome(self):
        print("Hello! Let's start calculationg the ROI percentage for your rental property.\n")
        while True:
            rentalIncome = float(input("What is the monthly rent for your property? "))
            if type(rentalIncome) == float:
                break
            else:
                print("You must enter a numerical value.")
        while True:
            response = input("Is there anything else on your property that will generate income such as laundry, storage, etc? (Yes or No) ")
            if response.title() == "Yes":
                otherIncome = input("What is the total monthly income generated from them? ")
                break
            elif response.title() == "No":
                otherIncome = 0.00
                break
            else:
                print("Please enter a valid response (Yes or No).")
        self.income = rentalIncome + otherIncome
        print(f"\nYour total monthly income for this property is ${self.income}.\n")
        return self.income
    def TotalExpenses(self):
        while True:
            tax = float(input("How much do you pay in taxes on your property monthly? "))
            if type(tax) == float:
                break
            else:
                print("Please enter a numerical value.")
        while True:
            insurance = float(input("How much is the insurance for your rental property monthly? "))
            if type(insurance) == float:
                break
            else:
                print("Please enter a numerical value.")
        while True:
            response2 = input("Do you pay for any of the utilities on your rental property? (Yes or No) ")
            if response2.title() == "Yes":
                utilities = float(input("How much do you pay for utilities on your property monthly? "))
                if type(utilities) == float:
                    continue
                else:
                    print("Please enter a numerical value")
                break
            elif response2.title() == "No":
                utilities = 0.00
                break
            else:
                print("Please enter a valid response (Yes or No).")
        while True:
            repairs = float(input("How much do you pay in repairs monthly? "))
            if type(repairs) == float:
                break
            else:
                print("Please enter a numerical value.")
        while True:
            mortgage = float(input("How much is your monthly mortgage payment? "))
            if type(mortgage) == float:
                break
            else:
                print("Please enter a numerical value")
        while True:
            vacancy = float(input("How much do you set aside monthly for future vacancies? "))
            if type(vacancy) == float:
                break
            else:
                print("Please enter a numerical value.")
        while True:
            response3 = input("Do you have any other monthly expenses such as Property Management, Cap X, Lawn Services, Pest Control, HOA, etc? (Yes or No) ")
            otherExpenses = []
            if response3.title() == "Yes":
                while True:
                    response4= input("Please enter the amount for each expense one by one. When you are done, type 'Done'. ")
                    if response4.title() == "Done":
                        break
                    else:
                        try:
                            response4 = int(response4)
                            otherExpenses.append(response4)
                        except:
                            print("Please enter a numerical value or type 'Done' when finished.")
                break
            elif response3.title() == "No":
                otherExpenses.append(0.00)
                break
            else:
                print("Please enter a valid response (Yes or No).")
            return otherExpenses
        totalOtherExpenses = sum(otherExpenses)
        self.expenses = tax + insurance + totalOtherExpenses + utilities + repairs + vacancy + mortgage
        print(f"\nYour total monthly expenses for this property is ${self.expenses}.\n")
        return self.expenses
    def cashFlow(self):
        self.cashflow = self.income - self.expenses
        print(f"\nYour cash flow is how much you are making monthly after expenses are taken into account. Your cash flow for this property is ${self.cashflow} a month\n")
        return self.cashflow
    def ROI(self):
        while True:
            downpayment = float(input("What was the down payment for your rental property? "))
            if type(downpayment) == float:
                break
            else:
                print("Please enter a numerical value.")
        while True:
            closingcost = float(input("What was the closing cost for your rental property? "))
            if type(closingcost) == float:
                break
            else:
                print("Please enter a numerical value.")
        while True:
            response5 = input("Do you plan to do any repairs/renovations on your property prior to renting it out? (Yes or No)")
            if response5.title() == "Yes":
                repaircost = float(input("How much are repair/renovation costs? "))
                break
            elif response5.title() == "No":
                repaircost = 0.00
                break
            else:
                print("Please enter a valid response (Yes or No).")
        while True:
            response6 = input("Are there any other investments involved in property? (Yes or No) ")
            otherinitialexpenses = []
            if response6.title() == "Yes":
                while True:
                    response7= input("Please enter the amount for each expense one by one. When you are done, type 'Done'. ")
                    if response7.title() == "Done":
                        break
                    else:
                        try:
                            response7 = int(response7)
                            otherinitialexpenses.append(response7)
                        except:
                            print("Please enter a numerical value or type 'Done' when finished.")
                break
            elif response6.title() == "No":
                otherinitialexpenses.append(0.00)
                break
            else:
                print("Please enter a valid response (Yes or No).")
        initialexpenses = sum(otherinitialexpenses)
        totalinvestment = initialexpenses + downpayment + closingcost + repaircost
        annualcashflow = self.cashflow * 12
        self.ROIperc = (annualcashflow/totalinvestment) * 100
        print("\nCongratulations! Your ROI has been calculated!")
        print(f"\nYour ROI for this property is {self.ROIperc}%!\n")
        return self.ROIperc

Renter = ROICalculator()
Renter2 = ROICalculator()

def run():
    while True:
        Renter.TotalIncome()
        Renter.TotalExpenses()
        Renter.cashFlow()
        Renter.ROI()
        break
    while True:
        Renter.TotalIncome()
        Renter.TotalExpenses()
        Renter.cashFlow()
        Renter.ROI()
        break
run()
       

