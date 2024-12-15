import math
monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expense

projected_savings = math.floor(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest is: ${projected_savings}.")

