import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df= pd.read_csv(big_mac_file)

query_string = "(iso_a3 == 'ARG')"
print(query_string)
arg_df = df.query(query_string)
print(round(arg_df['dollar_price'].mean(),2))
print(round(arg_df['dollar_price'].max(),5))
min_df_idx = df['dollar_price'].idxmin
max_df_idx = df['dollar_price'].idxmax

max_item =df.loc[min_df_idx]