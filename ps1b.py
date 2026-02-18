# Get user inputs
annual_salary = float(input("enter you annual salary: "))
portion_saved = float(input("enter you precent of your salary to save,as in decimal: "))
total_cost = float(input("enter the cost of your dream house: "))
semi_annual_raise = float(input("enter semi annual raise as a decimal "))


current_savings = 0
down_payment = total_cost * 0.25
monthly_salary = annual_salary / 12
months = 0
annual_return_rate = 0.04  # annual interest rate

# Calculate months needed
while (current_savings < down_payment):
    current_savings =current_savings+(current_savings * annual_return_rate) / 12
    current_savings = current_savings+(monthly_salary * portion_saved)
    months += 1

    if (months % 6 == 0):
        monthly_salary = monthly_salary*(1 + semi_annual_raise)

print("Months needed:", months)