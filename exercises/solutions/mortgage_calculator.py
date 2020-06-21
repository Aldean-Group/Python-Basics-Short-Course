# THIS DOES NOT ACCOUNT FOR MORTGAGE & LEGAL FEES OR STAMP DUTY TAX

#Take input
property_price = float(input("What is the price of the property?: £"))
deposit_paid = float(input("How much will your deposit be?: £"))
mortgage_term = int(input("How long is your mortgage term?(years): "))
interest_rate = float(input("What is the monthly interest rate on this mortgage?(percent): "))/1200

#Compute payments
owe = property_price - deposit_paid
monthly_payment = (owe * interest_rate / (1 - (1 / (1 + interest_rate) ** (mortgage_term * 12))))
yearly_payment = monthly_payment * 12

#Outputs
print()
print("Your monthly repayment is: £" + "{:.2f}".format(monthly_payment))
print("This means you'll pay £" + "{:.2f}".format(yearly_payment) + " yearly.")
print("You will have paid £" + "{:.2f}".format(yearly_payment * mortgage_term) + " overall.")
