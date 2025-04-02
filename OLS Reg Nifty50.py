import pandas as pd
import statsmodels.api as sm


# importing data
nifty50 = pd.read_csv("nifty50.csv")
nifty_midcap50 = pd.read_csv("niftymidcap50.csv")

# keeping only close prices (variables of interest)
nifty_50 = nifty50['Close']
nifty_midcap_50 = nifty_midcap50['Close']

# OLS Linear Regression
# to check the dependence of Nifty Midcap 50 prices on Nifty 50 prices

nifty_50 = sm.add_constant(nifty_50)         # adding intercept term
nifty_50.columns = ['const', 'Nifty50']      # changing column names

# Fitting model
model = sm.OLS(nifty_midcap_50, nifty_50).fit()
print(model.summary())