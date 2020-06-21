#Take inputs
age = int(input("Please enter your current age: "))
retirement_age = int(input("At what age do you plan to retire: "))
desired = float(input("Please enter the amount of money you desire to have at " + str(retirement_age) + ": "))
income_streams = int(input("Please enter the number of income streams you currently have: "))
print("")

#Sum up all income streams
cumulative_annum_income = 0
for i in range(0,income_streams):
    suffixes = {0: "st",
    1: "nd",
    2: "rd"}
    income_source = float(input(str(i + 1) + suffixes.get(i, "th") + " income generates (per annum): "))
    cumulative_annum_income += income_source

print("\nSo you currently make " + str(cumulative_annum_income) + " per year. \n")

#Find years taken and at what age they will be
years_taken = desired / cumulative_annum_income
age_reached = age + years_taken

print("It will take you " + str(int(years_taken)) + " years to earn " + str(desired) + ".")
print("You will be " + str(int(age_reached)) + " years old when you reach this amount.")

#Find how far ahead/behind schedule they are
difference = abs(age_reached - retirement_age)
if age_reached < retirement_age:
    #this fancy format technique just displays 2 dp accuracy instead of a long number
    print("This means you're " + "{:.2f}".format(difference) + " years ahead of your goal! Yay!")
#If behind schedule print how much more they'll need to earn per year to reach target
elif age_reached > retirement_age:
    print("So, on current progress, you're " + str(int(difference)) + " years behind schedule!")
    years_left = retirement_age - age #years until retirement
    min_needed = desired / years_left #minimum annual income needed to reach it
    amount_increase = min_needed - cumulative_annum_income #how much your current income must increase by
    print("You will need to increase your income by minimum " + str(amount_increase) + " per year to reach your goal! Goodluck!")
elif age_reached == retirement_age:
    print("You are right on track to acheive your desired goal at your desired age!")



