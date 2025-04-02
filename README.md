# nifty50

# Nifty Indices Regression Analysis

## Overview
This project analyzes the relationship between Nifty 50 and Nifty Midcap 50 indices using linear regression to understand how midcap prices depend on the main index.

## Requirements
- Python 3.x
- pandas
- statsmodels

## Data
Requires two CSV files:
- `nifty50.csv`
- `niftymidcap50.csv`

Both with 'Close' price columns.

## Usage
```
python nifty_regression.py
```

## Implementation
The script:
1. Loads both indices' closing prices
2. Adds a constant term to Nifty 50 values
3. Runs OLS regression to find the relationship
4. Prints statistical summary showing correlation strength and significance

The output helps determine how closely midcap prices follow the main index, useful for investment strategies and market analysis.
