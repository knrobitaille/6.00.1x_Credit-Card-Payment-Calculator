# Credit Card Payment Calculator

print("Welcome to the credit card payment calculator. Based on your balance, interest rate, and payment pattern, this calculator will show you if you will pay off your balance in a year and how much interest you will have paid.")

balance = float(input("Enter your credit card balance: "))

while True:
    annualInterestRate = float(input("Enter your credit card interest rate as a decimal: "))
    monthlyInterestRate = annualInterestRate/12
    if annualInterestRate >= 1:
        print("This rate is equal to "+str(annualInterestRate*100)+' %.')
        interestConfirm = input("Do you want to continue with this rate? Please enter 'y' or 'n : ")
        if interestConfirm in ["Y","y","yes","Yes","YES"]:
            break
    else:
        break

while True:
    paymentType = input("Do you plan to pay a fixed or variable amount? Please enter 'F' or 'V : ")
    if paymentType in ["F","f","V","v"]:
        break

if paymentType == "V" or paymentType == "v":    
    monthlyPaymentRate = float(input("Enter what percent of your balance you plan to pay each month (as a decimal): "))
    
    month = 0
    b = balance
    paid = 0

    while month < 12:
        p = b * monthlyPaymentRate
        ub = b - p
        b = ub * monthlyInterestRate + ub 
        paid += p
        month +=1
        print("Month " + str(month) + " Remaining balance:" + str(round(b,2)))
    if round(b,2) <= 0:
        print("You paid off your balance and paid " + str(round(paid-balance,2)) + " in interest.")
    else:
        print("You did not pay off the whole balance.")
    
elif paymentType == "F" or paymentType == "f":   
    monthlyPayment = float(input("Enter what fixed amount you plan to pay each month: "))

    month = 0
    b = balance
    paid = 0
    
    while month < 12:
        if b < monthlyPayment:
            p = b
        else:
            p =  monthlyPayment
        ub = b - p
        b = ub * monthlyInterestRate + ub 
        paid += p
        month +=1
        print("Month " + str(month) + " Remaining balance:" + str(max(round(b,2),0)))
    if b <= 0:
        print("You paid off your balance and paid " + str(round(paid-balance,2)) + " in interest.")
    else:
        print("You did not pay off the whole balance.")
else:
    print("Sorry, something went wrong.")

