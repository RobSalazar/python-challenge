#Modules
import os
import csv
import pandas as pd

sales = "Profit/Losses"

#Set our path
bdcsvpath = os.path.join("resources", "budget_data.csv")

headers = ["Date", sales]
dataframe = pd.read_csv(bdcsvpath, usecols=headers)

#The total number of months included in the dataset 
months = dataframe["Date"].count()
#The net total amount of "Profit/Losses"
netprof_loss = dataframe[sales].sum()
#Calculate the changes in "Profit/Losses" over entire period, and find the average for the changes
changeavg = dataframe[sales].diff().mean()
#print(changeavg)
#The greatest increase in profits (date and amount) over the entire period
maxsales = dataframe[sales].diff().max()
maxdate = dataframe[sales].max()
#DATE and amount
maxdate = dataframe.loc[dataframe[sales] == maxdate, "Date"]
maxdateloc = maxdate.iloc[0]
#print(maxdateloc)
#The greatest decrease in profits (date and amount) over the entire period
#Added min sales to get the Profit/Losses greatest decrease
minsales = dataframe[sales].diff().min()
mindate = dataframe[sales].min()
mindate = dataframe.loc[dataframe[sales] == mindate, "Date"]
mindateloc = mindate.iloc[0]
#print(mindateloc)
#print(maxsales)

#Printing out the results in my terminal
print("Financial Analysis" + "\n")
print("------------------------" + "\n")
print(f"Total Month: {months}" + "\n")
print(f"Total: {netprof_loss}" + "\n")
print(f"Average Change: {changeavg}" +"\n")
print(f"Greatest Increase in Profits: {maxdateloc} (${maxsales})" + "\n")
print(f"Greatest Decrease in Profits: {mindateloc} (${minsales})" + "\n")

#Creating a new .txt file in my analysis folder with my results
txtpath = os.path.join("analysis", "financialanalysis.txt")
with open(txtpath, "w") as txtfile:
    txtfile.write("Financial Analysis" + "\n")
    txtfile.write("------------------------" + "\n")
    txtfile.write(f"Total Month: {months}" + "\n")
    txtfile.write(f"Total: {netprof_loss}" + "\n")
    txtfile.write(f"Average Change: {changeavg}" +"\n")
    txtfile.write(f"Greatest Increase in Profits: {maxdateloc} (${maxsales})" + "\n")
    txtfile.write(f"Greatest Decrease in Profits: {mindateloc} (${minsales})" + "\n")
