# THIS CALCULATOR ONLY ACCOUNTS FOR STANDARD PERSONAL ALLOWANCE - HENCE CALCULATED ON GROSS WITH NO OTHER DEDUCTIONS
# WE ARE NOT FACTORING IN NATIONAL INSURANCE COSTS

# In future england/wales may have different rates but for now they are the same
rates = {
    "england": [[0, 37500, 0.2], [37501, 150000, 0.4], [150001, float('inf'), 0.45]],
    "wales": [[0, 37500, 0.2], [37501, 150000, 0.4], [150001, float('inf'), 0.45]],
    "scotland": [[0, 2085, 0.19], [2086, 12658, 0.2], [12659, 30930, 0.21], [30931, 150000, 0.41], [150001, float('inf'), 0.46]]
}

personal_allowance = 12500  # default allowance for 2020
tax_rate = list

#finding which country the user is in
while True:
    country = str.lower(input("Are you in England/Wales/Scotland?: "))
    if country == "england":
        tax_rate = rates.get("england") 
        break
    elif country == "wales":
        tax_rate = rates.get("wales")
        break
    elif country == "scotland":
        tax_rate = rates.get("scotland")
        break
    else:
        print("Are you sure you spelt that correctly with no spaces?\n")
        continue

#finding the users gross income
while True:
    try:
        gross_income = int(input("What is your gross income per annum?: £"))
    except ValueError:
        print("Sorry, I didn't understand that please enter gross income as a number!\n")
        continue
    else:
        break

#finding the users personal income
if(gross_income > 100000):
    # decrease the personal allowance by £1 for every £2 over 100k
    personal_allowance -= (gross_income - 100000)/2
    # take the maximum value between the allowance or 0. this prevents negative allowance.
    personal_allowance = max(personal_allowance, 0) #max function returns the highest of given values

#finding the users taxable income
taxable_income = gross_income - personal_allowance
taxable_income = max(taxable_income, 0)

#finding how much the user will pay by summing up the result of the tiered band system
total_tax = 0
pay_per_band = []
for band in tax_rate:
    if taxable_income > band[0] and taxable_income > band[1]:
        pay_per_band.append((band[1]-band[0]) * band[2])
    elif taxable_income > band[0] and taxable_income <= band[1]:
        pay_per_band.append((taxable_income-band[0]) * band[2])

total_tax = (sum(pay_per_band))

#Output to the user
print()#blank line space
print("Gross Income: £" + str(float(gross_income)))
print("Personal Allowance: £" + str(float(personal_allowance)))
print("Taxable Income: £" + str(float(taxable_income)))
print("Tax paid: £" + str(float(total_tax)))
print("Net Income: £" + str(float(gross_income - total_tax)))
