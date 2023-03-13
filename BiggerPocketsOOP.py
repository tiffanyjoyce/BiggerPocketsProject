class ROICalculator():

    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.cashflow = 0
        self.ROIperc = 0
    def TotalIncome(self):
        print("\nHello! Let's start calculationg the ROI percentage for your rental property.\n")
        print("We will start by calculating the total income being generated from the property.\n")
        while True:
            rentalIncome = input("What is the monthly rent for your property? ")
            try:
                rentalIncome = float(rentalIncome)
                break
            except:
                print("You must enter a numerical value.")
        while True:
            response = input("Is there anything else on your property that will generate income such as laundry, storage, etc? (Yes or No) ")
            otherIncome = []
            if response.title() == "Yes":
                while True:
                    r1= input("Please enter the amount for each form of income one by one. When you are done, type 'Done'. ")
                    if r1.title() == "Done":
                        break
                    else:
                        try:
                            r1 = float(r1)
                            otherIncome.append(r1)
                        except:
                            print("Please enter a numerical value or type 'Done' when finished.")
                break
            elif response.title() == "No":
                otherIncome.append(0.00)
                break
            else:
                print("Please enter a valid response (Yes or No).")
        otherIncomeSum = sum(otherIncome)
        self.income = rentalIncome + otherIncomeSum
        self.income = round(self.income, 2)
        print(f"\nYour total monthly income for this property is ${self.income}.\n")
        return self.income
    def TotalExpenses(self):
        print("Now we will calculate the total expenses involved in this property.\n")
        while True:
            tax = input("How much do you pay in taxes on your property monthly? ")
            try:
                tax = float(tax)
                break
            except:
                print("Please enter a numerical value.")
        while True:
            insurance = input("How much is the insurance for your rental property monthly? ")
            try:
                insurance = float(insurance)
                break
            except:
                print("Please enter a numerical value.")
        while True:
            response2 = input("Do you pay for any of the utilities on your rental property? (Yes or No) ")
            if response2.title() == "Yes":
                utilities = input("How much do you pay for utilities on your property monthly? ")
                try:
                    utilities = float(utilities)
                    break
                except:
                    print("Please enter a numerical value")
                break
            elif response2.title() == "No":
                utilities = 0.00
                break
            else:
                print("Please enter a valid response (Yes or No).")
        while True:
            repairs = input("How much do you pay in repairs monthly? ")
            try:
                repairs = float(repairs)
                break
            except:
                print("Please enter a numerical value.")
        while True:
            mortgage = input("How much is your monthly mortgage payment? ")
            try:
                mortgage = float(mortgage)
                break
            except:
                print("Please enter a numerical value")
        while True:
            vacancy = input("How much do you set aside monthly for future vacancies? ")
            try:
                vacancy = float(vacancy)
                break
            except:
                print("Please enter a numerical value.")
        while True:
            response3 = input("Do you have any other monthly expenses such as Property Management, Cap X, Lawn Services, Pest Control, HOA, etc? (Yes or No) ")
            otherExpenses = []
            if response3.title() == "Yes":
                while True:
                    response4= input("Please enter the amount for each expense one by one pressing enter after each one. When you are done, type 'Done'. ")
                    if response4.title() == "Done":
                        break
                    else:
                        try:
                            response4 = float(response4)
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
        self.expenses = round(self.expenses,2)
        print(f"\nYour total monthly expenses for this property cost ${self.expenses}.\n")
        return self.expenses
    def cashFlow(self):
        self.cashflow = self.income - self.expenses
        self.cashflow = round(self.cashflow,2)
        print(f"\nYour cash flow is how much you are making monthly after expenses are taken into account. Your cash flow for this property is ${self.cashflow} a month\n")
        return self.cashflow
    def ROI(self):
        print("We are almost there!\n")
        print("Finally, we will ask a couple of questions regarding the investments put into this property.\n")
        while True:
            downpayment = input("What was the down payment for your rental property? ")
            try:
                downpayment = float(downpayment)
                break
            except:
                print("Please enter a numerical value.")
        while True:
            closingcost = input("What was the closing cost for your rental property? ")
            try:
                closingcost = float(closingcost)
                break
            except:
                print("Please enter a numerical value.")
        while True:
            response5 = input("Do you plan to do any repairs/renovations on your property prior to renting it out? (Yes or No) ")
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
                    response7= input("Please enter the amount for each investment one by one. When you are done, type 'Done'. ")
                    if response7.title() == "Done":
                        break
                    else:
                        try:
                            response7 = float(response7)
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
        self.ROIperc = round(self.ROIperc,2)
        print("\nCongratulations! Your ROI has been calculated!")
        print(f"\nYour ROI for this property is {self.ROIperc}%!\n")
        return self.ROIperc

Renter = ROICalculator()
Renter2 = ROICalculator()

def run():
    Renter.TotalIncome()
    Renter.TotalExpenses()
    Renter.cashFlow()
    Renter.ROI()
    Renter2.TotalIncome()
    Renter2.TotalExpenses()
    Renter2.cashFlow()
    Renter2.ROI()
run()
       

