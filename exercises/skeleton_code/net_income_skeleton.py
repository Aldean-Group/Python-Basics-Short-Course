# THIS CALCULATOR ONLY ACCOUNTS FOR STANDARD PERSONAL ALLOWANCE - HENCE CALCULATED ON GROSS WITH NO OTHER DEDUCTIONS
# WE ARE NOT FACTORING IN NATIONAL INSURANCE COSTS

# In future england/wales may have different rates but for now they are the same
rates = {
    "england": [[0, 37500, 0.2], [37501, 150000, 0.4], [150001, float('inf'), 0.45]],
    "wales": [[0, 37500, 0.2], [37501, 150000, 0.4], [150001, float('inf'), 0.45]],
    "scotland": [[0, 2085, 0.19], [2086, 12658, 0.2], [12659, 30930, 0.21], [30931, 150000, 0.41], [150001, float('inf'), 0.46]]
}

personal_allowance = 12500  # default allowance for 2020

country = str.lower(input("Are you in England/Wales/Scotland?: "))
gross_income = int(input("What is your gross income per annum?: £"))

#finding how much the user will pay by summing up the result of the tiered band system
total_tax = 0
pay_per_band = []
for band in tax_rate:
    #TODO: Calculate the tax rate at each band and sum them together to find total tax!

#Output to user
print()#blank line space
print("Gross Income: £")
print("Personal Allowance: £")
print("Taxable Income: £")
print("Tax paid: £")
print("Net Income: £")

#TODO: For each £2 over £100,000 the personal allowance decreases by £1