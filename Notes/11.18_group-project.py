# %%
import os
import numpy as np
import pandas as pd

# %%
# Read in data
filename = 'score_details.csv'
filepath = os.path.join('..', '..', 'Forecasting21', 'weekly_results', filename)
data = pd.read_csv(filepath)

# %%
name_list_wk1 = []
name_list_wk2 = []
name_list_bon = []
for i in range(1,12):
    col_name_1 = 'wk'+str(i)+'_1wk.fcst'
    print(col_name_1)
    name_list_wk1.append(col_name_1)

    col_name_2 = 'wk'+str(i)+'_2wk.fcst'
    name_list_wk2.append(col_name_2)

    col_name_b = 'wk'+str(i)+'_bonus'
    name_list_bon.append(col_name_b)
    



# %%
