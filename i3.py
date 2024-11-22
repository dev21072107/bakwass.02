"""
print("Welcome to the Election Analysis App")

#Menu
def display_menu():
    print("\n--- Voting Analysis Menu ---")
    print("1. View Candidate Details")
    print("2. View Constituency Details")
    print("3. View Party Performance")
    print("4. Calculate Vote Percentages")
    print("5. View Overall Statistics")
    print("6. Save Statistics to File")
    print("7. Plot Graphs")
    print("8. Exit")
    

while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

import csv
import json
import matplotlib.pyplot as plt


# Define MP class
class MP:
    def __init__(self, name, party, constituency, votes):
        self.name = name
        self.party = party
        self.constituency = constituency
        self.votes = int(votes)

# Define Party class
class Party:
    def __init__(self, name):
        self.name = name
        self.total_votes = 0
        self.candidates = []

    def add_candidate(self, mp):
        self.candidates.append(mp)
        self.total_votes += mp.votes

# Define Constituency class
class Constituency:
    def __init__(self, name, country, total_voters, votes_cast):
        self.name = name
        self.country = country
        self.total_voters = int(total_voters)
        self.votes_cast = int(votes_cast)
        self.candidates = []

    def add_candidate(self, mp):
        self.candidates.append(mp)

# Load data from CSV

with open('EditedData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #print(row)
        counter1 = 0
        for party in parties:
            if row['First party'].lower() == party.lower():
                mpCount[counter1] += 1
            counter1 += 1    
        constituency = {'CName':row['Constituency name'],'RName':row['Region name'],'Country':row['Country name'],'CType':row['Constituency type'],'Party':row['First party']}
        con = Constituency(constituency)
        constituencies.append(con)
    counter1 = 0
    for party in parties:
        print(party, " got ",mpCount[counter1], " mps")
        counter1 += 1


 #Main
def main():
    file_path = 'EditedData.csv'
    parties, constituencies = load_data(file_path)


"""



import csv
import matplotlib.pyplot as plt

# Define the MP (Member of Parliament) class
class MP:
    def __init__(self, name, party, constituency, votes):
        self.name = name
        self.party = party
        self.constituency = constituency
        self.votes = int(votes)

# Define the Party class
class Party:
    def __init__(self, name):
        self.name = name
        self.total_votes = 0
        self.candidates = []

    def add_candidate(self, mp):
        """Add an MP to the party and update the party's total votes."""
        self.candidates.append(mp)
        self.total_votes += mp.votes

    def get_vote_percentage(self, total_votes_cast):
        """Calculate the percentage of total votes the party received."""
        return (self.total_votes / total_votes_cast) * 100 if total_votes_cast > 0 else 0

# Define the Constituency class
class Constituency:
    def __init__(self, name, country, total_voters, votes_cast):
        self.name = name
        self.country = country
        self.total_voters = int(total_voters)
        self.votes_cast = int(votes_cast)
        self.candidates = []

    def add_candidate(self, mp):
        """Add an MP to the constituency."""
        self.candidates.append(mp)

# Load data from the CSV file
def load_data(file_path):
    parties = {}
    constituencies = {}
    try:
        with open("EditedData.csv", mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                mp = MP(row['Candidate Name'], row['Party'], row['Seat Name'], row['Votes'])
                
                # Handle Party
                if row['Party'] not in parties:
                    parties[row['Party']] = Party(row['Party'])
                parties[row['Party']].add_candidate(mp)

                # Handle Constituency
                if row['Seat Name'] not in constituencies:
                    constituencies[row['Seat Name']] = Constituency(row['Seat Name'], row['Country'], row['Total Registered Voters'], row['Total Votes Cast'])
                constituencies[row['Seat Name']].add_candidate(mp)

    except FileNotFoundError:
        print("Error: CSV file not found.")
    except Exception as e:
        print(f"Error reading data: {e}")

    return parties, constituencies

# Display the menu of options to the user
def display_menu():
    print("\n--- Voting Analysis Menu ---")
    print("1. View Candidate Details")
    print("2. View Constituency Details")
    print("3. View Party Performance")
    print("4. Calculate Vote Percentages")
    print("5. View Overall Statistics")
    print("6. Save Statistics to File")
    print("7. Plot Graphs")
    print("8. Exit")

# Function to calculate overall statistics
def calculate_overall_statistics(parties, constituencies):
    total_votes = sum(party.total_votes for party in parties.values())
    total_candidates = sum(len(party.candidates) for party in parties.values())
    
    print(f"Total Votes Cast: {total_votes}")
    print(f"Total Candidates: {total_candidates}")
    
    # Calculate average votes per candidate
    avg_votes = total_votes / total_candidates if total_candidates > 0 else 0
    print(f"Average Votes per Candidate: {avg_votes:.2f}")
    
    # Calculate average vote percentage for each party
    for party in parties.values():
        for constituency in constituencies.values():
            percentage = party.get_vote_percentage(constituency.votes_cast)
            print(f"Party {party.name} received {percentage:.2f}% of votes in {constituency.name}.")

# Function to save the statistics to a file
def save_statistics(parties, constituencies, file_name="statistics.txt"):
    try:
        with open(file_name, "w") as file:
            for party in parties.values():
                file.write(f"Party: {party.name}\n")
                file.write(f"  Total Votes: {party.total_votes}\n")
                for constituency in constituencies.values():
                    percentage = party.get_vote_percentage(constituency.votes_cast)
                    file.write(f"  {constituency.name}: {percentage:.2f}% of total votes\n")
        print(f"Statistics saved to {file_name}.")
    except Exception as e:
        print(f"Error saving statistics: {e}")

# Function to plot party performance as a bar chart
def plot_party_performance(parties):
    party_names = [party.name for party in parties.values()]
    total_votes = [party.total_votes for party in parties.values()]
    
    plt.bar(party_names, total_votes, color='skyblue')
    plt.xlabel('Party')
    plt.ylabel('Total Votes')
    plt.title('Party Performance in General Election')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function to run the program
def main():
    file_path = 'EditedData.csv'  # Update with the correct path to the .csv file
    parties, constituencies = load_data(file_path)

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            # View Candidate Details
            candidate_name = input("Enter Candidate Name: ")
            found = False
            for party in parties.values():
                for candidate in party.candidates:
                    if candidate_name.lower() in candidate.name.lower():
                        print(f"{candidate.name} | Party: {candidate.party} | Constituency: {candidate.constituency} | Votes: {candidate.votes}")
                        found = True
            if not found:
                print("Candidate not found.")
        
        elif choice == '2':
            # View Constituency Details
            constituency_name = input("Enter Constituency Name: ")
            if constituency_name in constituencies:
                constituency = constituencies[constituency_name]
                print(f"{constituency.name} | Country: {constituency.country} | Voters: {constituency.total_voters} | Votes Cast: {constituency.votes_cast}")
                for candidate in constituency.candidates:
                    print(f"  {candidate.name} ({candidate.party}): {candidate.votes} votes")
            else:
                print("Constituency not found.")
        
        elif choice == '3':
            # View Party Performance
            for party_name, party in parties.items():
                print(f"{party_name}: Total Votes = {party.total_votes}")
        
        elif choice == '4':
            # Calculate Vote Percentages
            for constituency in constituencies.values():
                print(f"\nConstituency: {constituency.name}")
                for candidate in constituency.candidates:
                    percentage = (candidate.votes / constituency.votes_cast) * 100 if constituency.votes_cast > 0 else 0
                    print(f"{candidate.name} ({candidate.party}): {percentage:.2f}% of the votes")
        
        elif choice == '5':
            # View Overall Statistics
            calculate_overall_statistics(parties, constituencies)
        
        elif choice == '6':
            # Save Statistics to File
            save_statistics(parties, constituencies)
        
        elif choice == '7':
            # Plot Graphs
            plot_party_performance(parties)
        
        elif choice == '8':
            # Exit Program
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


                                  
       
        




