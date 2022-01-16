#Modules
import os
import pandas as pd

#Set our path
pollpath = os.path.join("resources", "election_data.csv")
headers = ["Voter ID" , "County" , "Candidate"]

df = pd.read_csv(pollpath, usecols=headers)
#groupeddf = df.groupby(["Candidate", df.index]).agg({"Candidate","Sum"})
#print(groupeddf)<---- maybe would of worked if i made a new column giving each candidate a summing amount of times their name came up

#The total number of votes cast (Voter ids shouldnt repeat so i figured unique was unnecessary)
totvotes = df["Voter ID"].count()
#print(totvotes) <---making sure this is working along the way

#A complete list of candidates who received votes
candlist = df["Candidate"].unique()
#print(candlist[0])

#The percentage of votes each candidate won
candcount = df["Candidate"].value_counts().astype(int)
khanperc = (candcount[0]/totvotes)*100
rkhan = khanperc.round(2)
correyperc = (candcount[1]/totvotes)*100
rcor = correyperc.round(2)
liperc = (candcount[2]/totvotes)*100
rli = liperc.round(2)
otooleyperc = (candcount[3]/totvotes)*100
rotoo = otooleyperc.round(2)

#print(rkhan) 

#The total number of votes each candidate won
khantot = candcount[0]
cortot = candcount[1]
litot = candcount[2]
otootot = candcount[3]

#print(khantot)
#The winner of the election based on popular vote.
winneramt = candcount.max()
khan = candlist[0]

#Print out the results to the terminal
print("Election Results" + "\n")
print("------------------------" + "\n")
print(f"Total Votes: {totvotes}" + "\n")
print("------------------------" + "\n")
print(f"{candlist[0]}: {rkhan}% ({khantot})" + "\n")
print(f"{candlist[1]}: {rcor}% ({cortot})" + "\n")
print(f"{candlist[2]}: {rli}% ({litot})" + "\n")
print(f"{candlist[3]}: {rotoo}% ({otootot})" + "\n")
print("------------------------" + "\n")
print(f"Winner: {khan}" + "\n")
print("------------------------" + "\n")

#Creating a new .txt file in my analysis folder with my results
txtpath = os.path.join("analysis", "election_analysis.txt")
with open(txtpath, "w") as txtfile:
    txtfile.write("Election Results" + "\n")
    txtfile.write("------------------------" + "\n")
    txtfile.write(f"Total Votes: {totvotes}" + "\n")
    txtfile.write("------------------------" + "\n")
    txtfile.write(f"{candlist[0]}: {rkhan}% ({khantot})" + "\n")
    txtfile.write(f"{candlist[1]}: {rcor}% ({cortot})" + "\n")
    txtfile.write(f"{candlist[2]}: {rli}% ({litot})" + "\n")
    txtfile.write(f"{candlist[3]}: {rotoo}% ({otootot})" + "\n")
    txtfile.write("------------------------" + "\n")
    txtfile.write(f"Winner: {khan}" + "\n")
    txtfile.write("------------------------" + "\n")

#Key notes and takeaways: I would have liked to mess around more with possibly adding a new column as a counter of sorts and utilizing that for my calculations
#also i tried using this rounding method on my pybank and could not get it to work but overall I am please with my results