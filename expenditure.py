import pandas as pd
import matplotlib.pyplot as plt
expenditure_df = pd.read_excel('Data files/uk_expenditure.xlsx')
plt.plot(expenditure_df['year'], expenditure_df['expenditure (£Bs)'], label='expenditure')
plt.plot(expenditure_df['year'], expenditure_df['revenue (£Bs)'], label='revenue')
plt.legend()
plt.show()
