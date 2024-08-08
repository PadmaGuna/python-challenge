# module for allowing to create file paths across operating systems
import os

# Module for reading CSV files
import csv

input_file_path = os.path.join('..', 'Resources', 'budget_data.csv')
output_file_path = os.path.join('..', 'Resources', 'fin_analysis.txt')


with open(input_file_path) as input_file:
    data_record = csv.reader(input_file, delimiter=',')
    print(data_record)

    # Read the header row first (skip this step if there is no header)
    data_header = next(data_record)
    
    # Read each row of data after the header
    total_months = 0
    total_profit_loss = 0
    greatest_incr_date = ""
    greatest_incr_amount = 0
    greatest_decr_date = ""
    greatest_decr_amount = 0
    
    for row in data_record:
        if int(row[1])> greatest_incr_amount:
            greatest_incr_amount = int(row[1])
            greatest_incr_date = row[0]

        if int(row[1])< greatest_decr_amount:
            greatest_decr_amount = int(row[1])
            greatest_decr_date = row[0]
        
        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(row[1])
        average_change = round(int(total_profit_loss) / int(total_months), 2)
    
    out_total_month = "Total Months : " + str(total_months) + "\n"
    out_total_profit = "Total : $ " + str(total_profit_loss) + "\n"
    out_average = "Average Change : " + f"{average_change : .2f}"  + "%\n"
    out_incr = "Greatest Increase in Profits : " + str(greatest_incr_date) + "  " + str(greatest_incr_amount) + "\n"
    out_decr = "Greatest Decrease in Profits : " + str(greatest_decr_date) + "  " + str(greatest_decr_amount) + "\n"
    
    print("Financial Analysis")
    print("----------------------")
    print(out_total_month)
    print(out_total_profit)
    print(out_average)
    print(out_incr)
    print(out_decr)
   
with open(output_file_path, "w") as outfile:
   #write the required info into the file
   outfile.write("Financial Analysis\n")
   outfile.write("----------------------\n")
   outfile.write(out_total_month)
   outfile.write(out_total_profit)
   outfile.write(out_average)
   outfile.write(out_incr)
   outfile.write(out_decr)
   
