#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv
import os

# Loading files and output
loading_file = os.path.join(".", "Resources", "budget_data.csv")
file_to_output = os.path.join(".", "budget_analysis.txt")

total_months = 0
total_net = 0

net_change_list = []
month_of_changes = []

greatest = ["", 0]
least = ["", 999999999999999999]

# Reading the csv and converting it into list
with open(loading_file) as financial_data:
    
    reader = csv.reader(financial_data)
    
    
    #Reading the header
    header = next(reader)
    
    #print(f"Header: {header}")
    first_row = next(reader)

    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
    total_months += 1
    
    for y in reader:
        
        #Tracking the total
        total_months = total_months + 1
        total_net += int(y[1])
        
        #Tracking the change
        net_change = int(y[1]) - previous_net
        previous_net = int(y[1])
        net_change_list.append(net_change)
        
        #Calculating the greatest increase
        if(net_change > greatest[1]):
            greatest[0] = y[0]
            greatest[1] = net_change
        
        #Calculating the greatest decrease
        if(net_change < least[1]):
            least[0] = y[0]
            least[1] = net_change
               
net_monthly_average = sum(net_change_list)/ len(net_change_list)



output = (
    f"Financial Analysis\n"
    f"--------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change ${net_monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest[0]} (${greatest[1]})\n"
    f"Greatest Decrease in Profits: {least[0]} (${least[1]})")

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
        


# In[ ]:





# In[ ]:




