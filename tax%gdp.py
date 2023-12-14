import pandas as pd
import matplotlib.pyplot as plt
tax_and_gdp = pd.read_excel('Data files/tax_and_gdp.xlsx')
correlation = tax_and_gdp['tax%gdp'].corr(tax_and_gdp['changegdp(%)'])
print(correlation)