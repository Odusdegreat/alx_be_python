# finance_calculator.py

# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings with 5% interest (simplified formula)
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output Results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings with 5% interest is: ${projected_annual_savings:.2f}")