income_streams = int(input("Please enter the number of income streams you currently have: "))
print()

suffixes = {0: "st",
    1: "nd",
    2: "rd"}

gross_income = 0
for i in range(0,income_streams):
    income_source = int(input(str(i + 1) + suffixes.get(i, "th") + " income generates (per annum): £"))
    gross_income += income_source

print("\nSo you currently make £" + str(gross_income) + " in gross income per year.")