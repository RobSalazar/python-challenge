#Modules
import os
import csv
import pandas as pd

sales = "Profit/Losses"

#Set our path
bdcsvpath = os.path.join("resources", "budget_data.csv")

headers = ["Date", sales]
df = pd.read_csv(bdcsvpath, usecols=headers)

#The total number of months included in the dataset 
months = df["Date"].count()
#The net total amount of "Profit/Losses"
netprof_loss = df[sales].sum()
#Calculate the changes in "Profit/Losses" over entire period, and find the average for the changes
