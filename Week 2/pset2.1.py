balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0

for i in range(1, 13):
    print("Month: " + str(i))
    minMonthlyPayment = round((balance * monthlyPaymentRate), 2)
    totalPaid += minMonthlyPayment
    print("Minimum monthly payment: " + str(minMonthlyPayment))
    remainingBalance = balance - minMonthlyPayment
    balance = round((remainingBalance + remainingBalance * annualInterestRate / 12.0), 2)
    print("Remaining balance: " + str(balance))
print("Total paid: " + str(totalPaid))
print("Remaining balance: " + str(balance))
    