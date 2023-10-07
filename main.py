import pandas as pd
import streamlit as st

if __name__ == '__main__':

    @st.cache_data
    def get_ownership():
        ownership = pd.read_csv('https://bbmtop1000.s3.us-east-2.amazonaws.com/ownership.csv')
        return ownership

    ownership = pd.read_csv('https://bbmtop1000.s3.us-east-2.amazonaws.com/ownership.csv')
    st.write('Player Ownership in Top 1000 Teams')
    ownership


    @st.cache_data
    def get_teams():
        teams_data = pd.read_csv('https://bbmtop1000.s3.us-east-2.amazonaws.com/teams_data.csv')
        return teams_data

    teams_data = get_teams()
    st.write('Top 1000 Teams')
    teams_data
