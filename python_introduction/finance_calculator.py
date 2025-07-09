# Get user input
monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your total monthly expenses: '))

# Calculate monthly and yearly savings
monthly_savings = monthly_income - monthly_expenses
yearly_savings = monthly_savings * 12

# Calculate projected savings with 5% interest
projected_savings = yearly_savings + (yearly_savings * 0.05)

# Display the results
print(f'Your monthly savings are ${monthly_savings}.')
print(f'Projected savings after one year, with interest, is: ${projected_savings}.')
