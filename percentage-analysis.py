# Import pandas

import pandas as pd

# Create dataset

table1 = pd.DataFrame({'Data':['Jan', 'Fev', 'Mar', 'Abr'], 'Values':[10,15,20,25]})

# Percentual change month over month

table1['pct_chg'] = table1.Values.pct_change().round(2)
table1

# Calculate proportions of a column with a single line of code

table1['pct'] = table1.Values.apply(lambda x: x/sum(table1.Values))
table1

# Plot bars behind numbers on a table

table1.style.bar(subset=['pct_chg', 'pct'], color='lightgreen')
