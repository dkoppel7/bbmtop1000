import pandas as pd
import streamlit as st

if __name__ == '__main__':

    @st.cache_data
    def get_ownership():
        ownership = pd.read_csv('https://bbmw5.s3.us-east-2.amazonaws.com/ownership.csv')
        ownership = ownership.drop('Unnamed: 0', axis=1)
        return ownership

    ownership = get_ownership()
    st.write('Player Ownership in Top 10000 Teams')
    ownership


    @st.cache_data
    def get_teams():
        teams_data = pd.read_csv('https://bbmw5.s3.us-east-2.amazonaws.com/teams_data.csv')
        teams_data = teams_data.drop('Unnamed: 0', axis=1)
        return teams_data

    teams_data = get_teams()
    st.write('Top 10000 Teams')
    teams_data
