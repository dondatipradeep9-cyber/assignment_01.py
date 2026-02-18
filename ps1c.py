# Part C: Finding the Right Amount to Save

annual_salary = float(input("Enter your annual salary: "))

total_cost = 1000000
down_payment = 0.25 * total_cost
annual_return = 0.04
semi_annual_raise = 0.07
months = 36

low = 0
high = 10000
epsilon = 100
steps = 0
best_rate = None


def calculate_savings(rate):
    current_savings = 0.0
    salary = annual_salary
    monthly_return = annual_return / 12

    for month in range(1, months + 1):
        current_savings += current_savings * monthly_return
        current_savings += (salary / 12) * rate

        if month % 6 == 0:
            salary += salary * semi_annual_raise

    return current_savings


# Check if it is possible to pay down payment
if calculate_savings(1.0) < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        rate = mid / 10000

        savings = calculate_savings(rate)

        if abs(savings - down_payment) <= epsilon:
            best_rate = rate
            break
        elif savings < down_payment:
            low = mid + 1
        else:
            high = mid - 1

    if best_rate is not None:
        print("Best savings rate:", round(best_rate, 4))
        print("Steps in bisection search:", steps)
    else:
        print("It is not possible to find a suitable saving rate.")

