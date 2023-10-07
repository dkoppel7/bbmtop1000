import pandas as pd
import streamlit as st

if __name__ == '__main__':

    files = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

    data = pd.read_csv('/Users/danielkoppel/Desktop/week_4/week4_1.csv')

    for f in files:
        d = pd.read_csv(f'/Users/danielkoppel/Desktop/week_4/week4_{f}.csv')
        data = pd.concat([data, d])

    top_teams = data.sort_values(by=['roster_points', 'username'], ascending = False).head(18000)
    ownership = pd.DataFrame(top_teams['player_name'].value_counts()).reset_index()
    ownership = ownership.rename(columns={'index': 'player_name', 'player_name': 'count'})
    st.write('Player Ownership in Top 1000 Teams')
    ownership

    teams_data = []
    index = 0
    while index < 18000:
        team_data = {}
        team = top_teams.iloc[index:(index + 18)]
        team_data['roster_points'] = team['roster_points'].values[0]
        team_data['username'] = team['username'].values[0]
        team_data['QBs'] = list(team[team['position_name'] == 'QB']['player_name'].value_counts().index)
        team_data['RBs'] = list(team[team['position_name'] == 'RB']['player_name'].value_counts().index)
        team_data['WRs'] = list(team[team['position_name'] == 'WR']['player_name'].value_counts().index)
        team_data['TEs'] = list(team[team['position_name'] == 'TE']['player_name'].value_counts().index)
        teams_data.append(team_data)
        index = index + 18

    teams_data = pd.DataFrame(teams_data)
    st.write('Top 1000 Teams')
    teams_data
