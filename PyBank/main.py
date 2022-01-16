#Modules
import os
import pandas as pd

#got tired of typing out "Profit/Losses"
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

#The greatest increase in profits (date and amount) over the entire period
maxsales = dataframe[sales].diff().max()
maxdate = dataframe[sales].max()
#Used this to locate the greatest increase in the data
maxdate = dataframe.loc[dataframe[sales] == maxdate, "Date"]
maxdateloc = maxdate.iloc[0]

#The greatest decrease in profits (date and amount) over the entire period
minsales = dataframe[sales].diff().min()
mindate = dataframe[sales].min()
#Used this to find the location of the greatest decrease date
mindate = dataframe.loc[dataframe[sales] == mindate, "Date"]
mindateloc = mindate.iloc[0]

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

#added notes: Since my 'min' and 'max' is giving the min and max of the change I ran another line for each getting the min and max without the change to give me 
#the correct dates that were shown in the example.