# Import csv and collections modules
import csv
from collections import defaultdict



# Open file in a dictionary
file = csv.DictReader(open("Resources/election_data.csv"))

# Print report title in console.
print("Election Results")
print("------------------------")



counter = defaultdict(int)
total_votes = 0
candidate = ""

for row in file:
    total_votes += 1
    counter[row['Candidate']] += 1
    candidate = row['Candidate']

candidates = dict(counter)

# Print total votes to console.
print(f"Total Votes: {total_votes}")
print("------------------")


candidate_details =[]
for key, value in candidates.items():
    percent_votes = (value/total_votes)
    # Print Candidate's votes percent and votes
    print(f"{key}: {percent_votes:.3%} ({value})")
    candidate_data = {"name": key, "percent_votes": percent_votes, "vote": value}
    candidate_details.append(candidate_data)
    

print("-----------------------")


winner = max(candidates, key=candidates.get) 

print(f"Winner: {winner}")
print("-----------------------")

# Write report in analysis file.
with open("./Analysis/election_result_analysis.csv","w") as output_file:
# Write Election Results reports.
    output_file.write("Election Results")
    output_file.write("\n")
    output_file.write("----------------------------")
    output_file.write("\n")

    # Write total votes to analysis file.
    output_file.write(f"Total Votes: {total_votes}")
    output_file.write("\n")
    output_file.write("\n")
    output_file.write("------------------")
    output_file.write("\n")
    for detail in candidate_details:    
        output_file.write(f"{detail['name']}: {detail['percent_votes']:.3%} ({detail['vote']})")
        output_file.write("\n")
    output_file.write("------------------")
    output_file.write("\n")
    output_file.write(f"Winner: {winner}")
    output_file.write("\n")
    output_file.write("------------------")


