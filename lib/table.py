import pandas as pd

df = pd.read_csv('Prem20232024Results.csv')

df_arsenal = df.loc[(df['HomeTeam'] == 'Arsenal') | (df['AwayTeam'] == 'Arsenal')]
df_aston_villa = df.loc[(df['HomeTeam'] == 'Aston Villa') | (df['AwayTeam'] == 'Aston Villa')]
df_bournemouth = df.loc[(df['HomeTeam'] == 'Bournemouth') | (df['AwayTeam'] == 'Bournemouth')]
df_brentford = df.loc[(df['HomeTeam'] == 'Brentford') | (df['AwayTeam'] == 'Brentford')]
df_brighton = df.loc[(df['HomeTeam'] == 'Brighton & Hove Albion') | (df['AwayTeam'] == 'Brighton & Hove Albion')]
df_burnley = df.loc[(df['HomeTeam'] == 'Burnley') | (df['AwayTeam'] == 'Burnley')]
df_chelsea = df.loc[(df['HomeTeam'] == 'Chelsea') | (df['AwayTeam'] == 'Chelsea')]
df_crystal_palace = df.loc[(df['HomeTeam'] == 'Crystal Palace') | (df['AwayTeam'] == 'Crystal Palace')]
df_everton = df.loc[(df['HomeTeam'] == 'Everton') | (df['AwayTeam'] == 'Everton')]
df_fulham = df.loc[(df['HomeTeam'] == 'Fulham') | (df['AwayTeam'] == 'Fulham')]
df_liverpool = df.loc[(df['HomeTeam'] == 'Liverpool') | (df['AwayTeam'] == 'Liverpool')]
df_luton = df.loc[(df['HomeTeam'] == 'Luton Town') | (df['AwayTeam'] == 'Luton Town')]
df_man_city = df.loc[(df['HomeTeam'] == 'Manchester City') | (df['AwayTeam'] == 'Manchester City')]
df_man_utd = df.loc[(df['HomeTeam'] == 'Manchester United') | (df['AwayTeam'] == 'Manchester United')]
df_newcastle = df.loc[(df['HomeTeam'] == 'Newcastle United') | (df['AwayTeam'] == 'Newcastle United')]
df_nottingham_forest = df.loc[(df['HomeTeam'] == 'Nottingham Forest') | (df['AwayTeam'] == 'Nottingham Forest')]
df_sheffield_united = df.loc[(df['HomeTeam'] == 'Sheffield United') | (df['AwayTeam'] == 'Sheffield United')]
df_tottenham = df.loc[(df['HomeTeam'] == 'Tottenham Hotspur') | (df['AwayTeam'] == 'Tottenham Hotspur')]
df_west_ham = df.loc[(df['HomeTeam'] == 'West Ham United') | (df['AwayTeam'] == 'West Ham United')]
df_wolves = df.loc[(df['HomeTeam'] == 'Wolverhampton Wanderers') | (df['AwayTeam'] == 'Wolverhampton Wanderers')]


df_arsenal.loc[(df_arsenal['HomeTeam'] == 'Arsenal') & (df_arsenal['Outcome'] == 'Home Win'), 'Points'] = 3
df_arsenal.loc[(df_arsenal['AwayTeam'] == 'Arsenal') & (df_arsenal['Outcome'] == 'Away Win'), 'Points'] = 3
df_arsenal.loc[(df_arsenal['HomeTeam'] == 'Arsenal') & (df_arsenal['Outcome'] == 'Draw'), 'Points'] = 1
df_arsenal.loc[(df_arsenal['AwayTeam'] == 'Arsenal') & (df_arsenal['Outcome'] == 'Draw'), 'Points'] = 1
df_arsenal.loc[(df_arsenal['HomeTeam'] == 'Arsenal') & (df_arsenal['Outcome'] == 'Away Win'), 'Points'] = 0
df_arsenal.loc[(df_arsenal['AwayTeam'] == 'Arsenal') & (df_arsenal['Outcome'] == 'Home Win'), 'Points'] = 0

arsenalpoints = df_arsenal['Points'].sum()
print(arsenalpoints)

df_aston_villa.loc[(df_aston_villa['HomeTeam'] == 'Aston Villa') & (df_aston_villa['Outcome'] == 'Home Win'), 'Points'] = 3
df_aston_villa.loc[(df_aston_villa['AwayTeam'] == 'Aston Villa') & (df_aston_villa['Outcome'] == 'Away Win'), 'Points'] = 3
df_aston_villa.loc[(df_aston_villa['HomeTeam'] == 'Aston Villa') & (df_aston_villa['Outcome'] == 'Draw'), 'Points'] = 1
df_aston_villa.loc[(df_aston_villa['AwayTeam'] == 'Aston Villa') & (df_aston_villa['Outcome'] == 'Draw'), 'Points'] = 1
df_aston_villa.loc[(df_aston_villa['HomeTeam'] == 'Aston Villa') & (df_aston_villa['Outcome'] == 'Away Win'), 'Points'] = 0
df_aston_villa.loc[(df_aston_villa['AwayTeam'] == 'Aston Villa') & (df_aston_villa['Outcome'] == 'Home Win'), 'Points'] = 0

aston_villapoints = df_aston_villa['Points'].sum()
print(aston_villapoints)

df_bournemouth.loc[(df_bournemouth['HomeTeam'] == 'Bournemouth') & (df_bournemouth['Outcome'] == 'Home Win'), 'Points'] = 3
df_bournemouth.loc[(df_bournemouth['AwayTeam'] == 'Bournemouth') & (df_bournemouth['Outcome'] == 'Away Win'), 'Points'] = 3
df_bournemouth.loc[(df_bournemouth['HomeTeam'] == 'Bournemouth') & (df_bournemouth['Outcome'] == 'Draw'), 'Points'] = 1
df_bournemouth.loc[(df_bournemouth['AwayTeam'] == 'Bournemouth') & (df_bournemouth['Outcome'] == 'Draw'), 'Points'] = 1
df_bournemouth.loc[(df_bournemouth['HomeTeam'] == 'Bournemouth') & (df_bournemouth['Outcome'] == 'Away Win'), 'Points'] = 0
df_bournemouth.loc[(df_bournemouth['AwayTeam'] == 'Bournemouth') & (df_bournemouth['Outcome'] == 'Home Win'), 'Points'] = 0

bournemouthpoints = df_bournemouth['Points'].sum()
print(bournemouthpoints)

df_brentford.loc[(df_brentford['HomeTeam'] == 'Brentford') & (df_brentford['Outcome'] == 'Home Win'), 'Points'] = 3
df_brentford.loc[(df_brentford['AwayTeam'] == 'Brentford') & (df_brentford['Outcome'] == 'Away Win'), 'Points'] = 3
df_brentford.loc[(df_brentford['HomeTeam'] == 'Brentford') & (df_brentford['Outcome'] == 'Draw'), 'Points'] = 1
df_brentford.loc[(df_brentford['AwayTeam'] == 'Brentford') & (df_brentford['Outcome'] == 'Draw'), 'Points'] = 1
df_brentford.loc[(df_brentford['HomeTeam'] == 'Brentford') & (df_brentford['Outcome'] == 'Away Win'), 'Points'] = 0
df_brentford.loc[(df_brentford['AwayTeam'] == 'Brentford') & (df_brentford['Outcome'] == 'Home Win'), 'Points'] = 0

brentfordpoints = df_brentford['Points'].sum()
print(brentfordpoints)

df_brighton.loc[(df_brighton['HomeTeam'] == 'Brighton & Hove Albion') & (df_brighton['Outcome'] == 'Home Win'), 'Points'] = 3
df_brighton.loc[(df_brighton['AwayTeam'] == 'Brighton & Hove Albion') & (df_brighton['Outcome'] == 'Away Win'), 'Points'] = 3
df_brighton.loc[(df_brighton['HomeTeam'] == 'Brighton & Hove Albion') & (df_brighton['Outcome'] == 'Draw'), 'Points'] = 1
df_brighton.loc[(df_brighton['AwayTeam'] == 'Brighton & Hove Albion') & (df_brighton['Outcome'] == 'Draw'), 'Points'] = 1
df_brighton.loc[(df_brighton['HomeTeam'] == 'Brighton & Hove Albion') & (df_brighton['Outcome'] == 'Away Win'), 'Points'] = 0
df_brighton.loc[(df_brighton['AwayTeam'] == 'Brighton & Hove Albion') & (df_brighton['Outcome'] == 'Home Win'), 'Points'] = 0

brightonpoints = df_brighton['Points'].sum()
print(brightonpoints)

df_burnley.loc[(df_burnley['HomeTeam'] == 'Burnley') & (df_burnley['Outcome'] == 'Home Win'), 'Points'] = 3
df_burnley.loc[(df_burnley['AwayTeam'] == 'Burnley') & (df_burnley['Outcome'] == 'Away Win'), 'Points'] = 3
df_burnley.loc[(df_burnley['HomeTeam'] == 'Burnley') & (df_burnley['Outcome'] == 'Draw'), 'Points'] = 1
df_burnley.loc[(df_burnley['AwayTeam'] == 'Burnley') & (df_burnley['Outcome'] == 'Draw'), 'Points'] = 1
df_burnley.loc[(df_burnley['HomeTeam'] == 'Burnley') & (df_burnley['Outcome'] == 'Away Win'), 'Points'] = 0
df_burnley.loc[(df_burnley['AwayTeam'] == 'Burnley') & (df_burnley['Outcome'] == 'Home Win'), 'Points'] = 0

burnleypoints = df_burnley['Points'].sum()
print(burnleypoints)

df_chelsea.loc[(df_chelsea['HomeTeam'] == 'Chelsea') & (df_chelsea['Outcome'] == 'Home Win'), 'Points'] = 3
df_chelsea.loc[(df_chelsea['AwayTeam'] == 'Chelsea') & (df_chelsea['Outcome'] == 'Away Win'), 'Points'] = 3
df_chelsea.loc[(df_chelsea['HomeTeam'] == 'Chelsea') & (df_chelsea['Outcome'] == 'Draw'), 'Points'] = 1
df_chelsea.loc[(df_chelsea['AwayTeam'] == 'Chelsea') & (df_chelsea['Outcome'] == 'Draw'), 'Points'] = 1
df_chelsea.loc[(df_chelsea['HomeTeam'] == 'Chelsea') & (df_chelsea['Outcome'] == 'Away Win'), 'Points'] = 0
df_chelsea.loc[(df_chelsea['AwayTeam'] == 'Chelsea') & (df_chelsea['Outcome'] == 'Home Win'), 'Points'] = 0

chelseapoints = df_chelsea['Points'].sum()
print(chelseapoints)

df_crystal_palace.loc[(df_crystal_palace['HomeTeam'] == 'Crystal Palace') & (df_crystal_palace['Outcome'] == 'Home Win'), 'Points'] = 3
df_crystal_palace.loc[(df_crystal_palace['AwayTeam'] == 'Crystal Palace') & (df_crystal_palace['Outcome'] == 'Away Win'), 'Points'] = 3
df_crystal_palace.loc[(df_crystal_palace['HomeTeam'] == 'Crystal Palace') & (df_crystal_palace['Outcome'] == 'Draw'), 'Points'] = 1
df_crystal_palace.loc[(df_crystal_palace['AwayTeam'] == 'Crystal Palace') & (df_crystal_palace['Outcome'] == 'Draw'), 'Points'] = 1
df_crystal_palace.loc[(df_crystal_palace['HomeTeam'] == 'Crystal Palace') & (df_crystal_palace['Outcome'] == 'Away Win'), 'Points'] = 0
df_crystal_palace.loc[(df_crystal_palace['AwayTeam'] == 'Crystal Palace') & (df_crystal_palace['Outcome'] == 'Home Win'), 'Points'] = 0

crystal_palacepoints = df_crystal_palace['Points'].sum()
print(crystal_palacepoints)

df_everton.loc[(df_everton['HomeTeam'] == 'Everton') & (df_everton['Outcome'] == 'Home Win'), 'Points'] = 3
df_everton.loc[(df_everton['AwayTeam'] == 'Everton') & (df_everton['Outcome'] == 'Away Win'), 'Points'] = 3
df_everton.loc[(df_everton['HomeTeam'] == 'Everton') & (df_everton['Outcome'] == 'Draw'), 'Points'] = 1
df_everton.loc[(df_everton['AwayTeam'] == 'Everton') & (df_everton['Outcome'] == 'Draw'), 'Points'] = 1
df_everton.loc[(df_everton['HomeTeam'] == 'Everton') & (df_everton['Outcome'] == 'Away Win'), 'Points'] = 0
df_everton.loc[(df_everton['AwayTeam'] == 'Everton') & (df_everton['Outcome'] == 'Home Win'), 'Points'] = 0

evertonpoints = df_everton['Points'].sum()
print(evertonpoints)

df_fulham.loc[(df_fulham['HomeTeam'] == 'Fulham') & (df_fulham['Outcome'] == 'Home Win'), 'Points'] = 3
df_fulham.loc[(df_fulham['AwayTeam'] == 'Fulham') & (df_fulham['Outcome'] == 'Away Win'), 'Points'] = 3
df_fulham.loc[(df_fulham['HomeTeam'] == 'Fulham') & (df_fulham['Outcome'] == 'Draw'), 'Points'] = 1
df_fulham.loc[(df_fulham['AwayTeam'] == 'Fulham') & (df_fulham['Outcome'] == 'Draw'), 'Points'] = 1
df_fulham.loc[(df_fulham['HomeTeam'] == 'Fulham') & (df_fulham['Outcome'] == 'Away Win'), 'Points'] = 0
df_fulham.loc[(df_fulham['AwayTeam'] == 'Fulham') & (df_fulham['Outcome'] == 'Home Win'), 'Points'] = 0

fulhampoints = df_fulham['Points'].sum()
print(fulhampoints)

df_liverpool.loc[(df_liverpool['HomeTeam'] == 'Liverpool') & (df_liverpool['Outcome'] == 'Home Win'), 'Points'] = 3
df_liverpool.loc[(df_liverpool['AwayTeam'] == 'Liverpool') & (df_liverpool['Outcome'] == 'Away Win'), 'Points'] = 3
df_liverpool.loc[(df_liverpool['HomeTeam'] == 'Liverpool') & (df_liverpool['Outcome'] == 'Draw'), 'Points'] = 1
df_liverpool.loc[(df_liverpool['AwayTeam'] == 'Liverpool') & (df_liverpool['Outcome'] == 'Draw'), 'Points'] = 1
df_liverpool.loc[(df_liverpool['HomeTeam'] == 'Liverpool') & (df_liverpool['Outcome'] == 'Away Win'), 'Points'] = 0
df_liverpool.loc[(df_liverpool['AwayTeam'] == 'Liverpool') & (df_liverpool['Outcome'] == 'Home Win'), 'Points'] = 0

liverpoolpoints = df_liverpool['Points'].sum()
print(liverpoolpoints)

df_luton.loc[(df_luton['HomeTeam'] == 'Luton Town') & (df_luton['Outcome'] == 'Home Win'), 'Points'] = 3
df_luton.loc[(df_luton['AwayTeam'] == 'Luton Town') & (df_luton['Outcome'] == 'Away Win'), 'Points'] = 3
df_luton.loc[(df_luton['HomeTeam'] == 'Luton Town') & (df_luton['Outcome'] == 'Draw'), 'Points'] = 1
df_luton.loc[(df_luton['AwayTeam'] == 'Luton Town') & (df_luton['Outcome'] == 'Draw'), 'Points'] = 1
df_luton.loc[(df_luton['HomeTeam'] == 'Luton Town') & (df_luton['Outcome'] == 'Away Win'), 'Points'] = 0
df_luton.loc[(df_luton['AwayTeam'] == 'Luton Town') & (df_luton['Outcome'] == 'Home Win'), 'Points'] = 0

lutonpoints = df_luton['Points'].sum()
print(lutonpoints)

df_man_city.loc[(df_man_city['HomeTeam'] == 'Manchester City') & (df_man_city['Outcome'] == 'Home Win'), 'Points'] = 3
df_man_city.loc[(df_man_city['AwayTeam'] == 'Manchester City') & (df_man_city['Outcome'] == 'Away Win'), 'Points'] = 3
df_man_city.loc[(df_man_city['HomeTeam'] == 'Manchester City') & (df_man_city['Outcome'] == 'Draw'), 'Points'] = 1
df_man_city.loc[(df_man_city['AwayTeam'] == 'Manchester City') & (df_man_city['Outcome'] == 'Draw'), 'Points'] = 1
df_man_city.loc[(df_man_city['HomeTeam'] == 'Manchester City') & (df_man_city['Outcome'] == 'Away Win'), 'Points'] = 0
df_man_city.loc[(df_man_city['AwayTeam'] == 'Manchester City') & (df_man_city['Outcome'] == 'Home Win'), 'Points'] = 0

man_citypoints = df_man_city['Points'].sum()
print(man_citypoints)

df_man_utd.loc[(df_man_utd['HomeTeam'] == 'Manchester United') & (df_man_utd['Outcome'] == 'Home Win'), 'Points'] = 3
df_man_utd.loc[(df_man_utd['AwayTeam'] == 'Manchester United') & (df_man_utd['Outcome'] == 'Away Win'), 'Points'] = 3
df_man_utd.loc[(df_man_utd['HomeTeam'] == 'Manchester United') & (df_man_utd['Outcome'] == 'Draw'), 'Points'] = 1
df_man_utd.loc[(df_man_utd['AwayTeam'] == 'Manchester United') & (df_man_utd['Outcome'] == 'Draw'), 'Points'] = 1
df_man_utd.loc[(df_man_utd['HomeTeam'] == 'Manchester United') & (df_man_utd['Outcome'] == 'Away Win'), 'Points'] = 0
df_man_utd.loc[(df_man_utd['AwayTeam'] == 'Manchester United') & (df_man_utd['Outcome'] == 'Home Win'), 'Points'] = 0

man_utdpoints = df_man_utd['Points'].sum()
print(man_utdpoints)

df_newcastle.loc[(df_newcastle['HomeTeam'] == 'Newcastle United') & (df_newcastle['Outcome'] == 'Home Win'), 'Points'] = 3
df_newcastle.loc[(df_newcastle['AwayTeam'] == 'Newcastle United') & (df_newcastle['Outcome'] == 'Away Win'), 'Points'] = 3
df_newcastle.loc[(df_newcastle['HomeTeam'] == 'Newcastle United') & (df_newcastle['Outcome'] == 'Draw'), 'Points'] = 1
df_newcastle.loc[(df_newcastle['AwayTeam'] == 'Newcastle United') & (df_newcastle['Outcome'] == 'Draw'), 'Points'] = 1
df_newcastle.loc[(df_newcastle['HomeTeam'] == 'Newcastle United') & (df_newcastle['Outcome'] == 'Away Win'), 'Points'] = 0
df_newcastle.loc[(df_newcastle['AwayTeam'] == 'Newcastle United') & (df_newcastle['Outcome'] == 'Home Win'), 'Points'] = 0

newcastlepoints = df_newcastle['Points'].sum()
print(newcastlepoints)

df_nottingham_forest.loc[(df_nottingham_forest['HomeTeam'] == 'Nottingham Forest') & (df_nottingham_forest['Outcome'] == 'Home Win'), 'Points'] = 3
df_nottingham_forest.loc[(df_nottingham_forest['AwayTeam'] == 'Nottingham Forest') & (df_nottingham_forest['Outcome'] == 'Away Win'), 'Points'] = 3
df_nottingham_forest.loc[(df_nottingham_forest['HomeTeam'] == 'Nottingham Forest') & (df_nottingham_forest['Outcome'] == 'Draw'), 'Points'] = 1
df_nottingham_forest.loc[(df_nottingham_forest['AwayTeam'] == 'Nottingham Forest') & (df_nottingham_forest['Outcome'] == 'Draw'), 'Points'] = 1
df_nottingham_forest.loc[(df_nottingham_forest['HomeTeam'] == 'Nottingham Forest') & (df_nottingham_forest['Outcome'] == 'Away Win'), 'Points'] = 0
df_nottingham_forest.loc[(df_nottingham_forest['AwayTeam'] == 'Nottingham Forest') & (df_nottingham_forest['Outcome'] == 'Home Win'), 'Points'] = 0

nottingham_forestpoints = df_nottingham_forest['Points'].sum()
print(nottingham_forestpoints)

df_sheffield_united.loc[(df_sheffield_united['HomeTeam'] == 'Sheffield United') & (df_sheffield_united['Outcome'] == 'Home Win'), 'Points'] = 3
df_sheffield_united.loc[(df_sheffield_united['AwayTeam'] == 'Sheffield United') & (df_sheffield_united['Outcome'] == 'Away Win'), 'Points'] = 3
df_sheffield_united.loc[(df_sheffield_united['HomeTeam'] == 'Sheffield United') & (df_sheffield_united['Outcome'] == 'Draw'), 'Points'] = 1
df_sheffield_united.loc[(df_sheffield_united['AwayTeam'] == 'Sheffield United') & (df_sheffield_united['Outcome'] == 'Draw'), 'Points'] = 1
df_sheffield_united.loc[(df_sheffield_united['HomeTeam'] == 'Sheffield United') & (df_sheffield_united['Outcome'] == 'Away Win'), 'Points'] = 0
df_sheffield_united.loc[(df_sheffield_united['AwayTeam'] == 'Sheffield United') & (df_sheffield_united['Outcome'] == 'Home Win'), 'Points'] = 0

sheffield_unitedpoints = df_sheffield_united['Points'].sum()
print(sheffield_unitedpoints)

df_tottenham.loc[(df_tottenham['HomeTeam'] == 'Tottenham Hotspur') & (df_tottenham['Outcome'] == 'Home Win'), 'Points'] = 3
df_tottenham.loc[(df_tottenham['AwayTeam'] == 'Tottenham Hotspur') & (df_tottenham['Outcome'] == 'Away Win'), 'Points'] = 3
df_tottenham.loc[(df_tottenham['HomeTeam'] == 'Tottenham Hotspur') & (df_tottenham['Outcome'] == 'Draw'), 'Points'] = 1
df_tottenham.loc[(df_tottenham['AwayTeam'] == 'Tottenham Hotspur') & (df_tottenham['Outcome'] == 'Draw'), 'Points'] = 1
df_tottenham.loc[(df_tottenham['HomeTeam'] == 'Tottenham Hotspur') & (df_tottenham['Outcome'] == 'Away Win'), 'Points'] = 0
df_tottenham.loc[(df_tottenham['AwayTeam'] == 'Tottenham Hotspur') & (df_tottenham['Outcome'] == 'Home Win'), 'Points'] = 0

tottenhampoints = df_tottenham['Points'].sum()
print(tottenhampoints)

df_west_ham.loc[(df_west_ham['HomeTeam'] == 'West Ham United') & (df_west_ham['Outcome'] == 'Home Win'), 'Points'] = 3
df_west_ham.loc[(df_west_ham['AwayTeam'] == 'West Ham United') & (df_west_ham['Outcome'] == 'Away Win'), 'Points'] = 3
df_west_ham.loc[(df_west_ham['HomeTeam'] == 'West Ham United') & (df_west_ham['Outcome'] == 'Draw'), 'Points'] = 1
df_west_ham.loc[(df_west_ham['AwayTeam'] == 'West Ham United') & (df_west_ham['Outcome'] == 'Draw'), 'Points'] = 1
df_west_ham.loc[(df_west_ham['HomeTeam'] == 'West Ham United') & (df_west_ham['Outcome'] == 'Away Win'), 'Points'] = 0
df_west_ham.loc[(df_west_ham['AwayTeam'] == 'West Ham United') & (df_west_ham['Outcome'] == 'Home Win'), 'Points'] = 0

west_hampoints = df_west_ham['Points'].sum()
print(west_hampoints)

df_wolves.loc[(df_wolves['HomeTeam'] == 'Wolverhampton Wanderers') & (df_wolves['Outcome'] == 'Home Win'), 'Points'] = 3
df_wolves.loc[(df_wolves['AwayTeam'] == 'Wolverhampton Wanderers') & (df_wolves['Outcome'] == 'Away Win'), 'Points'] = 3
df_wolves.loc[(df_wolves['HomeTeam'] == 'Wolverhampton Wanderers') & (df_wolves['Outcome'] == 'Draw'), 'Points'] = 1
df_wolves.loc[(df_wolves['AwayTeam'] == 'Wolverhampton Wanderers') & (df_wolves['Outcome'] == 'Draw'), 'Points'] = 1
df_wolves.loc[(df_wolves['HomeTeam'] == 'Wolverhampton Wanderers') & (df_wolves['Outcome'] == 'Away Win'), 'Points'] = 0
df_wolves.loc[(df_wolves['AwayTeam'] == 'Wolverhampton Wanderers') & (df_wolves['Outcome'] == 'Home Win'), 'Points'] = 0

wolvespoints = df_wolves['Points'].sum()
print(wolvespoints)


d = {'Teams': ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton & Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Liverpool', 'Luton Town', 'Manchester City', 'Manchester United', 'Newcastle United', 'Nottingham Forest', 'Sheffield United', 'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers'],
     'Points': [arsenalpoints, aston_villapoints, bournemouthpoints, brentfordpoints, brightonpoints, burnleypoints, chelseapoints, crystal_palacepoints, evertonpoints, fulhampoints, liverpoolpoints, lutonpoints, man_citypoints, man_utdpoints, newcastlepoints, nottingham_forestpoints, sheffield_unitedpoints, tottenhampoints, west_hampoints, wolvespoints]}

df_epltable = pd.DataFrame(data=d)
epltable = df_epltable.sort_values(by=['Points'], ascending=False)
print(epltable)