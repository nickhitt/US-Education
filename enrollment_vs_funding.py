exec(open("load_data.py").read())

import seaborn as sns
import numpy as np

import statsmodels.api as sm

states = states_all["STATE"].unique()

for state in states
    df = states_all[states_all["STATE"] == state]
    model = sm.OLS(df["GRADES_ALL_G"], df["TOTAL_EXPENDITURE"])

