import pandas as pd
import numpy as np

results = pd.read_csv("Prem20232024Results.csv")
home_score = results.HomeScore
away_score = results.AwayScore

max_home_score = np.max(home_score)
max_away_score = np.max(away_score)
min_home_score = np.min(home_score)
min_away_score = np.min(away_score)

print(max_home_score)
print(max_away_score)
print(min_home_score)
print(min_away_score)

def highest_home_score_margin(max_home_score, min_away_score):
    return np.diff((max_home_score, min_away_score))

print(highest_home_score_margin(6, 1))
