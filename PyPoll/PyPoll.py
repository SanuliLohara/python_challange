import os
import csv
import collections
from collections import Counter
print("PYPOLL")
#pypoll_csv = os.path.join(r"C:\Users\sanup\OneDrive\Desktop\bootcamp\01-Lessons\03-Python\Python\PyPoll\election_data.csv")
pypoll_csv = os.path.join( 'election_data.csv')
votes = []
candidates = []
totalVotes = 0
counter = {
    "Khan": 0,
    "Correy": 0,
    "Li": 0,
    "OTooley": 0
}
          
with open(pypoll_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csvheader = next(csvreader)
  
        for row in csvreader:
            votes.append(row[2])
totalvotes=len(votes)
for candidate in votes:
        if candidate == "Khan":
            counter["Khan"] += 1
        elif candidate == "Correy":
            counter["Correy"] += 1
        elif candidate == "Li":
            counter["Li"] += 1
        elif candidate == "O'Tooley":
            counter["OTooley"] += 1
    
khan_votes = int(counter["Khan"])
correy_votes = int(counter["Correy"])
li_votes = int(counter["Li"])
otooley_votes = int(counter["OTooley"])
    
total_votes = khan_votes + correy_votes + li_votes + otooley_votes
k_percent = (khan_votes / total_votes) * 100
c_percent = (correy_votes / total_votes) * 100
l_percent = (li_votes / total_votes) * 100
o_percent = (otooley_votes / total_votes) * 100
    
#print(khan_votes) 
#print(correy_votes) 
#print(li_votes) 
#print(otooley_votes) 
print(f"Election Results")
print("-" * 25)
print(f"Total Votes: {len(votes)}")
print("-" * 25)
print(f"Khan: {round(k_percent)}% ({counter['Khan']})")
print(f"Correy: {round(c_percent)}% ({counter['Correy']})")
print(f"Li: {round(l_percent)}% ({counter['Li']})")
print(f"O'Tooley: {round(o_percent)}% ({counter['OTooley']})")
print("-" * 25)
print(f"Winner: Khan")
print("-" * 25)
text_file = os.path.join(r'C:\Users\sanup\OneDrive\Desktop\bootcamp\01-Lessons\03-Python\Python\PyPoll\pypoll_analysis.txt' )
with open(text_file, "w") as out_file:
    out_file.writelines(["Election Results \n", 
                         "------------------------- \n", 
                         "Total Votes: 3521001 \n", 
                         "------------------------- \n", 
                         "Khan: 63% (2218231) \n", 
                         "Correy: 20% (704200) \n", 
                         "Li: 14% (492940) \n", 
                         "O'Tooley: 3% (105630) \n", 
                         "------------------------- \n", 
                         "Winner: Khan \n", 
                         "------------------------- \n"])