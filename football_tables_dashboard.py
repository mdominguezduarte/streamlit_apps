# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:14:41 2022

@author: DKu_7
"""

# Football Tables dashboard (EPL, LaLiga, Bundesliga)
# Data webscraped from the official websites

from bs4 import BeautifulSoup
import requests
import pandas as pd
import streamlit as st

### Webscraping Section To Obtain Data

## La Liga Table Webscraping
# Reference my own webscrape work:
# https://github.com/dk81/web_scrape_python/blob/main/laliga_spanishsoccer_webscrape.ipynb

laliga_url = "https://www.laliga.com/en-GB/laliga-santander/standing"

la_liga_response = requests.get(laliga_url)

laliga_soup = BeautifulSoup(la_liga_response.content, 'html.parser')

results = laliga_soup.find('div', 
        {'class': 'styled__StandingTableBody-e89col-5 cDiDQb'}).find_all('div', 
        {'class': 'styled__ContainerAccordion-e89col-11 HquGF'})
                                                                         
# Scraping La Liga Table with list comprehension

laliga_teams = [result.find('div', {'class': 'styled__ShieldContainer-lo8ov8-0 bkblFd shield-desktop'}).find('p', 
                {'class': 'styled__TextRegularStyled-sc-1raci4c-0 glrfl'}).get_text() 
                for result in results]

laliga_points = [result.find_all('p', 
         {'class': 'styled__TextRegularStyled-sc-1raci4c-0 cIcTog'})[0].get_text()
         for result in results]


laliga_played = [result.find_all('p', 
         {'class': 'styled__TextRegularStyled-sc-1raci4c-0 cIcTog'})[1].get_text()
         for result in results]

laliga_wins = [result.find_all('p', 
         {'class': 'styled__TextRegularStyled-sc-1raci4c-0 cIcTog'})[2].get_text()
         for result in results]

laliga_draws = [result.find_all('p', 
         {'class': 'styled__TextRegularStyled-sc-1raci4c-0 cIcTog'})[3].get_text()
         for result in results]

laliga_losses = [result.find_all('p', 
         {'class': 'styled__TextRegularStyled-sc-1raci4c-0 cIcTog'})[4].get_text()
         for result in results]

laliga_goals_for = [result.find_all('p', 
         {'class': 'styled__TextRegularStyled-sc-1raci4c-0 cIcTog'})[5].get_text()
         for result in results]

laliga_goals_against = [result.find_all('p', 
         {'class': 'styled__TextRegularStyled-sc-1raci4c-0 cIcTog'})[6].get_text()
         for result in results]

laliga_goals_diff = [result.find_all('p', 
         {'class': 'styled__TextRegularStyled-sc-1raci4c-0 cIcTog'})[7].get_text()
         for result in results]             

## Make pandas Dataframe of La Liga table:

laliga_df = pd.DataFrame({'Rank': range(1, len(laliga_teams) + 1), 'Team': laliga_teams, 
                          'Pts': laliga_points, 'Pl': laliga_played, 
                          'W': laliga_wins, 'D': laliga_draws, 
                          'L': laliga_losses, 'GF': laliga_goals_for, 
                          'GA': laliga_goals_against, 'GD': laliga_goals_diff})        

## ------------
## Premier League Table Webscraping
# Reference own work: https://github.com/dk81/web_scrape_python/blob/main/epl_table_webscrape.ipynb

epl_link = "https://www.premierleague.com/tables"

response = requests.get(epl_link)

epl_soup = BeautifulSoup(response.content, 'html.parser')

# Table rows are in the tr tags. Each table row is for each EPL team
epl_table_rows = epl_soup.find_all('tr')

# Rank, Teams, Number of Games Played:
epl_rank = [row.find_all('span', {'class': 'value'})[0].get_text() for row in epl_table_rows[1:40:2]]
epl_teams = [row.find_all('span', {'class': 'long'})[0].get_text() for row in epl_table_rows[1:40:2]]
epl_played = [row.find_all('td')[3].get_text() for row in epl_table_rows[1:40:2]]

# Wins, Draws, Losses
epl_wins = [row.find_all('td')[4].get_text() for row in epl_table_rows[1:40:2]]
epl_draws = [row.find_all('td')[5].get_text() for row in epl_table_rows[1:40:2]]
epl_losses = [row.find_all('td')[6].get_text() for row in epl_table_rows[1:40:2]]

# Goals For, Goals Against, Goal Diff & Points:
epl_goals_for = [row.find_all('td')[7].get_text() for row in epl_table_rows[1:40:2]]
epl_goals_against = [row.find_all('td')[8].get_text() for row in epl_table_rows[1:40:2]]
epl_goal_diff = [row.find_all('td')[9].get_text().strip() for row in epl_table_rows[1:40:2]]
epl_points = [row.find_all('td')[10].get_text().strip() for row in epl_table_rows[1:40:2]]

# Make EPL Table:
epl_df = pd.DataFrame({
         'Rank': epl_rank,
         'Team': epl_teams,
         'Pl': epl_played,
         'W': epl_wins,
         'D': epl_draws,
         'L': epl_losses,
         'GF': epl_goals_for,
         'GA': epl_goals_against,
         'GD': epl_goal_diff,
         'Pts': epl_points
})

## ------------
## Bundesliga Table Webscraping

bundesliga_url = "https://www.bundesliga.com/en/bundesliga/table"

response = requests.get(bundesliga_url)

bundes_soup = BeautifulSoup(response.content, 'html.parser')

bundes_results = bundes_soup.find('table', {'class': 'table'}).find_all('tr')

# Remove first row (header):
bundes_results = bundes_results[1:]

# Webscrape parts of the table I use list comprhension instead of for loop append method:

bundes_teams = [result.find('td', {'class': 'team'}).find('span', {'class': 'd-none d-lg-inline'}).get_text() 
                for result in bundes_results]
    
bundes_matches = [result.find('td', {'class': 'matches'}).get_text() for result in bundes_results]

bundes_points = [result.find('td', {'class': 'pts'}).get_text() for result in bundes_results]

bundes_wins = [result.find('td', {'class': 'd-none d-lg-table-cell wins'}).get_text() for result in bundes_results]

bundes_draws = [result.find('td', {'class': 'd-none d-lg-table-cell draws'}).get_text() for result in bundes_results]

bundes_losses = [result.find('td', {'class': 'd-none d-lg-table-cell looses'}).get_text() for result in bundes_results]

bundes_goals = [result.find('td', {'class': 'd-none d-md-table-cell goals'}).get_text() for result in bundes_results]

bundes_goal_diff = [result.find('td', {'class': 'difference'}).get_text().replace("+", "") for result in bundes_results]

## Make pandas Dataframe:
bundes_df = pd.DataFrame({'Rank': range(1, 19), 'Team': bundes_teams, 'Matches': bundes_matches,
                          'Points': bundes_points, 'Wins': bundes_wins, 'Draws': bundes_draws,
                          'Losses': bundes_losses, 'Goals': bundes_goals, 'Goal Difference': bundes_goal_diff})
    
# Split Goals Into Goals For & Goals Against:
bundes_df[['Goals For','Goals Against']] = bundes_df['Goals'].str.split(":",expand=True,)
    
# Drop Goals column
bundes_df.drop('Goals', axis = 1, inplace = True)
    
# Rearrange columns
bundes_df = bundes_df.reindex(columns=['Rank', 'Team', 'Matches', 'Points',
                         'Wins', 'Draws', 'Losses', 'Goals For',
                         'Goals Against', 'Goal Difference'])

bundes_df.columns = ['Rank', 'Team', 'Matches', 'Pts',
                     'W', 'D', 'L', 
                     'GF', 'GA', 'GD']

## ------------
## Serie A Table Webscraping

serieA_url = "https://www.legaseriea.it/en/serie-a/league-table"

serieA_response = requests.get(serieA_url)

serieA_soup = BeautifulSoup(serieA_response.content, 'html.parser')

serieA_table = serieA_soup.find('tbody')

table_rows = serieA_table.find_all('tr')

# Obtain parts of the table:
    
serieA_ranks = [row.find_all('td')[0].find('span').text for row in table_rows]

serieA_team_names = [row.find_all('td')[0].text.split()[1: ] for row in table_rows]

# Unnest lists, dealing with the Hellas Verona case pretty much
serieA_teams = [" ".join(str(x) for x in test) for test in serieA_team_names]

serieA_points = [row.find_all('td')[1].text for row in table_rows]

serieA_played = [row.find_all('td')[2].text for row in table_rows]

serieA_wins = [row.find_all('td')[3].text for row in table_rows]

serieA_draws = [row.find_all('td')[4].text for row in table_rows]

serieA_losses = [row.find_all('td')[5].text for row in table_rows]

serieA_goals_for = [row.find_all('td')[-2].text for row in table_rows]

serieA_goals_against = [row.find_all('td')[-1].text for row in table_rows]

# Make pandas Dataframe of Serie A table:

serieA_df = pd.DataFrame({'Rank': serieA_ranks, 'Team': serieA_teams, 'Pts': serieA_points,
                          'Played': serieA_played, 'W': serieA_wins, 'D': serieA_draws, 'L': serieA_losses, 
                          'GF': serieA_goals_for, 'GA': serieA_goals_against})

## ------------
## French Ligue 1 Table Webscraping

ligue_one_url = "https://www.ligue1.com/ranking"

ligue_one_response = requests.get(ligue_one_url)

ligue_one_soup = BeautifulSoup(ligue_one_response.content, 'html.parser')

table_rows = ligue_one_soup.find('div', {'class': 'classement-table-body'}).find('ul').find_all('li')

# Ranks
ligue_one_ranks = [x.find('a').find_all('div')[0].text for x in table_rows]

# Team Name
ligue_one_teams = [x.find('a').find_all('div')[1].find('span').text for x in table_rows]

# Points
ligue_one_points = [x.find('a').find_all('div')[2].text for x in table_rows]

# Played
ligue_one_played = [x.find('a').find_all('div')[3].text for x in table_rows]

# Wins
ligue_one_wins = [x.find('a').find_all('div')[4].text for x in table_rows]

# Draws
ligue_one_draws = [x.find('a').find_all('div')[5].text for x in table_rows]

# Losses
ligue_one_losses = [x.find('a').find_all('div')[6].text for x in table_rows]

# Goals For
ligue_one_goals_for = [x.find('a').find_all('div')[7].text for x in table_rows]

# Goals Against
ligue_one_goals_against = [x.find('a').find_all('div')[8].text for x in table_rows]

# Goal Difference
ligue_one_goals_diff = [x.find('a').find_all('div')[9].text for x in table_rows]

## Create Ligue 1 Dataframe
ligue1_df = pd.DataFrame({'Rank': ligue_one_ranks, 'Team': ligue_one_teams, 'Pts': ligue_one_points,
                           'Pl': ligue_one_played, 'W': ligue_one_wins, 'D': ligue_one_draws, 'L': ligue_one_losses, 
                           'GF': ligue_one_goals_for, 'GA': ligue_one_goals_against, 'GD': ligue_one_goals_diff})

##-------------
# Sidebar Radio Buttons Choice

st.sidebar.write("""
# Football League Tables
""")

# Table Based On Choice
league = st.sidebar.radio(
     "Select A League",
     ("Spain's La Liga", 'English Premier League', 'German Bundesliga',
      "Italy's Serie A", "France's Ligue 1"))

# Dictionary

st.sidebar.write("""
### Dictionary \n
            
W = # Wins \n
D = # Draws \n
L = # Losses \n
GF = Goals For \n 
GA = Goals Against \n
GD = Goals Difference      

"""         
)

# Remove indices:
# CSS to inject contained in a string
# Reference: https://docs.streamlit.io/knowledge-base/using-streamlit/hide-row-indices-displaying-dataframe
hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

### Front Page Area

st.write(f"""
         Today's Date: {pd.to_datetime("today").strftime('%B %d %Y')}
         """)
         
with st.expander("Info (Click To Expand)"):
     st.write("""
         This dashboard allows the user to see Football tables from Europe's top football league.
         Select a league from the left sidebar and the corresponding league table will appear.
     """)

         
# Show league table depending on choice from radio buttons:                
if league == "Spain's La Liga":
    st.write("### La Liga Table")
    st.table(laliga_df)
elif league == "English Premier League":
    st.write("### Premier League Table")
    st.table(epl_df)
elif league == "German Bundesliga":
    st.write("### Bundesliga Table")
    st.table(bundes_df)
elif league == "Italy's Serie A":
    st.write("### Serie A Table")
    st.table(serieA_df)
elif league == "France's Ligue 1":
    st.write("### Ligue 1 Table")
    st.table(ligue1_df)



                                                                             