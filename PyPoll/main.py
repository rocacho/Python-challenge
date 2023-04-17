# The Python file is running within the PyPoll Folder
import pandas as pd

# Reading the CSV file
df = pd.read_csv('./Resources/election_data.csv')

# Defining variables to create a complete list of candidates who received votes
# To caculate the percentage and total number of votes I used the method from...
# Softhints: Pandas count and percentage by value for a column 
# https://www.youtube.com/watch?v=P5pxJkv71BU
candidate = df.Candidate
percent = candidate.value_counts(normalize=True).mul(100).round(1).astype(str) + "%"
count = candidate.value_counts()

# To find the most frequent value to identify the winner
# To identify the most voted candidate I usede the method from NeuralNine: Most Frequent Value of A List...
# Python Tips and Tricks #15
# https://www.youtube.com/watch?v=JebCroMMFOQ
from collections import Counter
counter = Counter(candidate)
x = counter.most_common(1)[0]

# Defining Rows to print the result in the terminal

#Title
Title = print("Election Results"), print("---------------------------")

# Total number of votes cast
Total_votes = print('Total Votes: ' + df['Ballot ID'].count().astype(str)), print("---------------------------")

# The complete list of candidates who received votes with percents...
# and total number of votes each candidate won
Results_Summary = print(pd.DataFrame({'Percent': percent,'Count': count})), print("---------------------------")

# The winner of the election based on popular vote
Winner_is = print(f"Winner: {((x)[0])}"), print("---------------------------")

#Importing file to CSV
import csv 

with open('Election_Results.csv','w') as file:
    write = csv.writer(file)
    write.writerow({'Election Results'})
    write.writerow({'---------------------------'})
    write.writerow({'Total Votes: ' + df['Ballot ID'].count().astype(str)})
    write.writerow({'---------------------------'})
    write.writerow([pd.DataFrame({'Percent': percent,'Count': count})])
    write.writerow({'---------------------------'})
    write.writerow({(f"Winner: {((x)[0])}")})
    write.writerow({'---------------------------'})
