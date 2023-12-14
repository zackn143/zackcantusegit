import matplotlib.pyplot as plt
import pandas as pd

# 2020-2021 data
income_df1 = pd.read_csv('Data files/2020-2021.csv')
s = income_df1['Tax bracket (lower limit)'] = income_df1['Tax bracket (lower limit)'].str.replace(',', '').astype(int)
income_df1['taxpayers'] = income_df1['taxpayers'].str.replace(',', '').astype(int)
income_df1['Total income before tax'] = income_df1['Total income before tax'].str.replace(',', '').astype(int)
income_df1['Cumulative Total Income'] = income_df1['Total income before tax'].cumsum()
total_income = sum(income_df1['Total income before tax'])
total_taxpayers = sum(income_df1['taxpayers'])
income_df1['percentage_of_taxpayers'] = income_df1['taxpayers']/total_taxpayers
x = income_df1['Cumulative Percentage of Taxpayers'] = income_df1['percentage_of_taxpayers'].cumsum()
y = income_df1['cumulative_share_of_total_income'] = income_df1['Cumulative Total Income']/total_income
# 2019-2020 data
income_df2 = pd.read_csv('Data files/1920data.csv')
s2 = income_df2['Tax bracket (lower limit)'] = income_df2['Tax bracket (lower limit)'].str.replace(',', '').astype(int)
income_df2['taxpayers'] = income_df2['taxpayers'].str.replace(',', '').astype(int)
income_df2['Total income before tax'] = income_df2['Total income before tax'].str.replace(',', '').astype(int)
income_df2['Cumulative Total Income'] = income_df2['Total income before tax'].cumsum()
total_income2 = sum(income_df2['Total income before tax'])
total_taxpayers2 = sum(income_df2['taxpayers'])
income_df2['percentage_of_taxpayers'] = income_df2['taxpayers']/total_taxpayers2
x2 = income_df2['Cumulative Percentage of Taxpayers'] = income_df2['percentage_of_taxpayers'].cumsum()
y2 = income_df2['cumulative_share_of_total_income'] = income_df2['Cumulative Total Income']/total_income2

equality_y = x
fig, axs = plt.subplots(2, 2)
fig.suptitle('2020-2021')
axs[0,0].plot(x,y)
axs[0,1].plot(s,y)
axs[1,1].plot(x,s)
axs[0,0].plot(x,equality_y)
fig2, axs2 = plt.subplots(2, 2)
fig2.suptitle('2019-2020')
axs2[0,0].plot(x2,y2)
axs2[0,1].plot(s2,y2)
axs2[1,1].plot(x2,s2)
axs2[0,0].plot(x2,equality_y)
plt.show()