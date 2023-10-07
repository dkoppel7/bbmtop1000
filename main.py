import pandas as pd
import streamlit as st

if __name__ == '__main__':

    @st.cache_data
    def load_data():
        return pd.read_csv('https://bbmtop1000.s3.us-east-2.amazonaws.com/week4_master.csv')
    data = load_data()

    @st.cache_data
    def get_ownership():
        top_teams = data.sort_values(by=['roster_points', 'username'], ascending=False).head(18000)
        ownership = pd.DataFrame(top_teams['player_name'].value_counts()).reset_index()
        ownership = ownership.rename(columns={'index': 'player_name', 'player_name': 'count'})
        return top_teams, ownership
    
    top_teams, ownership = get_ownership()
    st.write('Player Ownership in Top 1000 Teams')
    ownership


    @st.cache_data
    def get_teams():
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
        return teams_data

    teams_data = get_teams()
    st.write('Top 1000 Teams')
    teams_data
