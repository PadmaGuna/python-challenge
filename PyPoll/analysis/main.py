# module for allowing to create file paths across operating systems
import os

# Module for reading CSV files
import csv

input_file_path = os.path.join('..', 'Resources', 'election_data.csv')
output_file_path = os.path.join('..', 'Resources', 'election_analysis.txt')

candi_list = []
candi_pct = []
candi_count = []
out_candi = []
total_vote_count = 0
#candi_list.append("")
#candi_count.append(0)
#candi_pct.append(0)
j = 0
winner_count = 0
with open(input_file_path) as input_file:
    data_record = csv.reader(input_file, delimiter=',')
    data_header = next(data_record)
    
    for row in data_record:
        total_vote_count += 1
        candidate_name = row[2]
        if candidate_name not in candi_list:
            candi_list.append(candidate_name)
            candi_count.append(1)
        else:
            candi_count[candi_list.index(candidate_name)] += 1    
    #Calculate Percent            
    for count in candi_count:
        pct = count/total_vote_count * 100
        candi_pct.append(pct)
    #Calculate the winner
    
    out_total_votes = "Total Votes : " + str(total_vote_count) + "\n"
    
    print("Election Results")
    print("----------------------")
    print(out_total_votes)
    print("----------------------")
    #print the output in required format and get the winner name
    for i in range(len(candi_list)):
        if candi_count[i] > winner_count:
            winner_count = candi_count[i]
            winner = candi_list[i]
        print(f"{candi_list[i]}: {candi_pct[i]:.3f}% ({candi_count[i]})\n")    
        
    print("----------------------")
    out_winner = "Winner : " + winner + " " + str(winner_count) + "\n"
    print(out_winner)
    print("----------------------")

with open(output_file_path, "w") as outfile:
  #write the required info into the file
   outfile.write("Election Results\n")
   outfile.write("----------------------\n")
   outfile.write(out_total_votes)
   outfile.write("----------------------\n")
   for i in range(len(candi_list)):
        outfile.write(f"{candi_list[i]}: {candi_pct[i]:.3f}% ({candi_count[i]})\n")
   outfile.write("----------------------\n")
   outfile.write(out_winner)
   outfile.write("----------------------\n")
   