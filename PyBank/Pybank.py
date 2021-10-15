import os
import csv
pybank_csv = (r'C:\Users\sanup\OneDrive\Desktop\Assignments\Python\PyBank\budget_data.csv')
print("PYBANK")

months = []
profit_loss_changes = []
count_months = 0
profit_loss = 0
profit_loss_change = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    for row in csvreader:
        count_months += 1
        current_month_profit_loss = int(row[1])
        profit_loss = profit_loss + current_month_profit_loss

    if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            

    else:

            # Compute change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

text_file = os.path.join(r'C:\Users\sanup\OneDrive\Desktop\bootcamp\01-Lessons\03-Python\Python\PyBank\pybank_analysis.txt')
with open(text_file, "w") as out_file:
    out_file.writelines(["Financial Analysis\n",
                         "----------------------------\n",
                         "Total Months:  {count_months}\n",
                         "Total:  ${profit_loss}\n",
                         "Average Change:  ${average_profit_loss}\n",
                         "Greatest Increase in Profits:  {best_month} (${highest_change})\n",
                         "Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n"])