# The Python file is running within the PyBank Folder
import pandas as pd

# Reading the CSV file
df = pd.read_csv('./Resources/budget_data.csv')

# Creating a new colum to calculate change using shift metodology
df['Profit/Losses-1'] = df['Profit/Losses'].shift(1)

# Substracting the new Column "Profit/Losses-1" to the original to get the change values
# To calculate Change used the method form Fervent: Calculating Stock Returns with Python(Code-along)
# https://www.youtube.com/watch?v=YBGnuEa-QKE
df['Change'] = df['Profit/Losses']- df['Profit/Losses-1']

#C alculating the total number of months included in the dataset... 
# and net total amount of "Profit/Losses" over the entire period
Total_Months = df['Date'].count()
Total = '$' + str(df['Profit/Losses'].sum())

# Calculating changes in "Profit/Losses" over the entire period...
# and the average of those changes
Average_Change = '$' + str(round(df['Change'].mean(),2))

# Calculating the greatest increase in profits (date and amount) over the entire period
# For the date I used iloc in combination with argmax & argmin to identify the index and find the date
# To find the date of the biggest change I used the method from...
# John Ortiz Ordoñez: Pandas - Ejercicio 142: Seleccionar el Índice de una Columna de un DataFrame con el Elemento Mayor
# https://www.youtube.com/watch?v=K0k933AXBqs
Greatest_Increase = str(df['Date'].iloc[df['Change'].argmax()]) +' (' + "$" + str(df['Change'].max()) + ")"
Greatest_Decrease = str(df['Date'].iloc[df['Change'].argmin()]) + ' (' + "$" + str(df['Change'].min()) + ")"

# Puting everything together to print in the terminal and in CSV file
print('Financial Analysis')
print("---------------------------")
Fincancial_Analysis = pd.Series([Total_Months,Total,Average_Change,Greatest_Increase,Greatest_Decrease], 
                                index=['Total Months:', 'Total:', 'Average Change:',
                                       'Greatest Increase in Profits:','Greatest Decrease in Profits:'])

Fincancial_Analysis.to_csv('Financial_Analysis.csv')

Fincancial_Analysis
