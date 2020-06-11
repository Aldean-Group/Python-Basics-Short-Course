retirement_age = int(input("At what age do you plan to retire: "))

desired = int(input("Please enter the amount of money you desire to have at " + str(retirement_age) + ": "))
age = int(input("Please enter your current age: "))
income_streams = int(input("Please enter the number of income streams you currently have: "))
print("")

cumulative_annum_income = 0
for i in range(0,income_streams):
    suffixes = {0: "st",
    1: "nd",
    2: "rd"}
    income_source = int(input(str(i + 1) + suffixes.get(i, "th") + " income generates (per annum): "))
    cumulative_annum_income += income_source

print("\nSo you currently make " + str(cumulative_annum_income) + " per year. \n")

years_taken = desired / cumulative_annum_income

print("It will take you " + f"{years_taken:.2f}" + " years to earn " + str(desired) + ".")
print("You will be " + str(int(age+years_taken)) + " years old when you reach this amount.")

#TODO: Show how much money they have to earn if they're short
#TODO: Show how many years early they acheived it if on track