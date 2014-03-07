balance = 4123
annualInterestRate = 0.18
fixedMonthlyPayment = 0
b = balance
a = annualInterestRate
while True:
    # loop over each month of a year
    for i in range(1, 13):
        remainingBalance = balance - fixedMonthlyPayment
        balance = round((remainingBalance + remainingBalance * annualInterestRate / 12.0), 2)
    # if the balance is less than or equals to zero, print out value of fixedMonthlyPayment, break the loop
    if balance <= 0:
        print("Lowest Payment: " + str(fixedMonthlyPayment))
        break
    else:
        # if the balance is not less than or equals to zero, increment fixedMonthlyPayment by 10, continue loop
        fixedMonthlyPayment += 10
        balance = b
        annualInterestRate = a