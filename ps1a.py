annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of salary to be saved (in decimal): "))
total_cost = float(input("Enter the cost of your dream house: "))

down_payment = 0.25 * total_cost
current_savings = 0
annual_return = 0.04
monthly_salary = annual_salary / 12
monthly_return = annual_return / 12
months = 0

while current_savings < down_payment:
    # Add investment return
    current_savings += current_savings * monthly_return
    
    # Add monthly savings from salary
    current_savings += monthly_salary * portion_saved
    
    months += 1

print("Number of months needed to save for the down payment:", months)
