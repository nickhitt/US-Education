import pandas as pd

exec(open("load_data.py").read())

import seaborn as sns
import numpy as np
import statsmodels.api as sm

states = states_all["STATE"].unique()
state_list = []
slope_list = []
for state in states:
    df = states_all[states_all["STATE"] == state][["ENROLL",
                                                   "TOTAL_EXPENDITURE"]].dropna(thresh=2)
    model = sm.OLS(df["ENROLL"], df["TOTAL_EXPENDITURE"]).fit()
    slope_list.append(model.params)
    state_list.append(state)

slopes = pd.DataFrame(slope_list)
exp_v_enroll = pd.DataFrame([state_list, slopes])