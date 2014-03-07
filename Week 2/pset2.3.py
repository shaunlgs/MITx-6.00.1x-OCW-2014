balance = 4123
annualInterestRate = 0.18
b = balance
a = annualInterestRate
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12)** 12) / 12.0
fixedMonthlyPayment = round((lowerBound + upperBound) / 2, 2)
while True:
    # loop over each month of a year
    for i in range(1, 13):
        remainingBalance = balance - fixedMonthlyPayment
        balance = round((remainingBalance + remainingBalance * annualInterestRate / 12.0), 2)
    # if the balance is near zero, print out value of fixedMonthlyPayment, break the loop
    if (abs(balance- 0)) < 0.1:
        print("Lowest Payment: " + str(round((fixedMonthlyPayment), 2)))
        break
    else:
        # if balance is less than zero, means fixedMonthlyPayment is too high
        if balance < 0:
            upperBound = fixedMonthlyPayment
        # if balance is more than zero, means fixedMonthlyPayment is too low
        elif balance > 0:
            lowerBound = fixedMonthlyPayment
        # try new fixedMonthlyPayment
        fixedMonthlyPayment = (lowerBound + upperBound) / 2
        balance = b
        annualInterestRate = a