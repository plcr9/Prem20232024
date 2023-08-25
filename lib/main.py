import pandas as pd

df = pd.read_csv('Prem20232024Results.csv')
df.to_html('results.html',index=False)