# Import csv module
import csv

# Report lists
total_months = []
total_profit = []
monthly_profit_change = []

# Open file in read mode.
with open("./Resources/budget_data.csv", "r") as budget_data:

     # File reader
    rows = csv.reader(budget_data, delimiter=",")

    # Skip the heading.
    header = next(rows)

    # Iterate through the rows.
    for row in rows:
        # Append the total months and total profit to their corresponding lists.
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through the profits - get the monthly change in profits.
    for i in range(len(total_profit)-1):
        # Append two months difference to monthly profit change.
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# Calculate max and min monthly profit change.
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Calculate increase and decrease using monthly profit change index.
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

# Print report in console
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


# Write report in analysis file.
output_file = "./Analysis/budget_analysis.csv"
with open(output_file,"w") as file:
# Write Financial Analysis report.
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")