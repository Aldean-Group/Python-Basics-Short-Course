#Take inputs
age = int(input("Please enter your current age: "))
retirement_age = int(input("At what age do you plan to retire: "))
desired = float(input("Please enter the amount of money you desire to have at " + str(retirement_age) + ": "))
income_streams = int(input("Please enter the number of income streams you currently have: "))
print("")

#Take value of each income stream
cumulative_annum_income = 0
for stream in range(0,income_streams):
    
