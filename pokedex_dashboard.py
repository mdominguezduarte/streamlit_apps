# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:21:11 2022

@author: DKu_7
"""

# Pokédex Dashboard With Webscraped Data from Pokemondb.net

import pandas as pd
from bs4 import BeautifulSoup
import requests
import streamlit as st

# Pokemon Db Table

url = "https://pokemondb.net/pokedex/all"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

results = soup.find('table', {'id': 'pokedex'}).find('tbody')

pokemon = results.find_all('tr')

# Obtain data into lists (list comprehension):

number = [p.find('td', {'class': "cell-num cell-fixed"}).get_text() for p in pokemon]

name = [p.find('td', {'class': "cell-name"}).get_text() for p in pokemon]

poke_type = [p.find('td', {'class': "cell-icon"}).get_text() for p in pokemon]

total = [p.find('td', {'class': "cell-total"}).get_text() for p in pokemon]

hp = [p.find_all('td', {'class': "cell-num"})[1].get_text() for p in pokemon]

attack = [p.find_all('td', {'class': "cell-num"})[2].get_text() for p in pokemon]

defense = [p.find_all('td', {'class': "cell-num"})[3].get_text() for p in pokemon]

sp_atk = [p.find_all('td', {'class': "cell-num"})[4].get_text() for p in pokemon]

sp_def = [p.find_all('td', {'class': "cell-num"})[5].get_text() for p in pokemon]

speed = [p.find_all('td', {'class': "cell-num"})[6].get_text() for p in pokemon]

## Make pandas Dataframe:

pokemon_df = pd.DataFrame({'Number': number, 'Pokémon': name, 'Type': poke_type,
                           'Total': total, 'HP': hp, 'Attack': attack,
                           'Defense': defense, 'Sp. Atk': sp_atk, 
                           'Sp. Def': sp_def, 'Speed': speed})

#----------------------------

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

#-------------------------

## Sidebar:

# Choose Search Option:
    
search_option = st.sidebar.radio(
                 "Enable Search Option",
                 ("Search Pokémon", 
                  'Search By Type', 
                  "Top 20 "))

# 1) Search bar for Pokemon:
pokemon_search = st.sidebar.text_area(label = "Option 1: Search for Pokémon.", value = "", max_chars = 40)

# 2) Search by type(s):
type_search = st.sidebar.selectbox(
                label = "Option 2: Search by Type",
                options = ['Any', 'Normal', 'Fire', 'Water', 'Grass', 'Electric', 'Ice',
                           'Fighting', 'Poison', 'Ground', 'Flying',
                           'Psychic', 'Bug', 'Rock', 'Ghost',
                           'Dark', 'Dragon', 'Steel', 'Fairy']
    )

# 3) Search Top 20:

top_search = st.sidebar.selectbox(
                label = "Option 3: Search Top 20 By Attribute",
                options = ['None',
                           'Top 20 Total Stats',
                           'Top 20 HP',
                           'Top 20 Attack',
                           'Top 20 Defense',
                           'Top 20 Special Attack',
                           'Top 20 Special Defense',
                           'Top 20 Speed'
                           ]
    )




#--------------------------
### Front Page Area

st.write("""
         # Pokédex Dashboard
         """)
         
with st.expander("Info (Click To Expand)"):
     st.write("""
         This dashboard allows the user to see the whole Pokédex and search for Pokémon. Data is webscraped from Pokemon.db.
         Select a search option on the left and use the corresponding to search for what you would like.
     """)
     
     
# Functions for each search case:
    
def top_total_stats(df):
    df['Total'] = pd.to_numeric(df['Total'])
    # Sort values:
    return_df = df.sort_values('Total', ascending = False).head(20)
    return(return_df)

def top_hp(df):
    df['HP'] = pd.to_numeric(df['HP'])
    # Sort values:
    return_df = df.sort_values('HP', ascending = False).head(20)
    return(return_df)

def top_attack(df):
    df['Attack'] = pd.to_numeric(df['Attack'])
    # Sort values:
    return_df = df.sort_values('Attack', ascending = False).head(20)
    return(return_df)

def top_defense(df):
    df['Defense'] = pd.to_numeric(df['Defense'])
    # Sort values:
    return_df = df.sort_values('Defense', ascending = False).head(20)
    return(return_df)

def top_sp_atk(df):
    df['Sp. Atk'] = pd.to_numeric(df['Sp. Atk'])
    # Sort values:
    return_df = df.sort_values('Sp. Atk', ascending = False).head(20)
    return(return_df)

def top_sp_def(df):
    df['Sp. Def'] = pd.to_numeric(df['Sp. Def'])
    # Sort values:
    return_df = df.sort_values('Sp. Def', ascending = False).head(20)
    return(return_df)

def top_speed(df):
    df['Speed'] = pd.to_numeric(df['Speed'])
    # Sort values:
    return_df = df.sort_values('Speed', ascending = False).head(20)
    return(return_df)

# If statements based on sidebar choices:
    
if search_option == "Search Pokémon":
    df = pokemon_df[pokemon_df['Pokémon'].str.contains(pokemon_search)]
elif (search_option == "Search By Type") & (type_search != "Any"):
    df = pokemon_df[pokemon_df['Type'].str.contains(type_search)]
elif top_search == "Top 20 Total Stats":
    st.write("## Top 20 Pokémon By Total Stats")
    df = top_total_stats(pokemon_df)  
elif top_search == "Top 20 HP":
    st.write("## Top 20 Pokémon By HP")
    df = top_hp(pokemon_df)  
elif top_search == "Top 20 Attack":
    st.write("## Top 20 Pokémon By Attack")
    df = top_attack(pokemon_df)  
elif top_search == "Top 20 Defense":
    st.write("## Top 20 Pokémon By Defense")
    df = top_defense(pokemon_df)  
elif top_search == "Top 20 Special Attack":
    st.write("## Top 20 Pokémon By Special Attack")
    df = top_sp_atk(pokemon_df)  
elif top_search == "Top 20 Special Defense":
    st.write("## Top 20 Pokémon By Special Defense")
    df = top_sp_def(pokemon_df)  
elif top_search == "Top 20 Speed":
    st.write("## Top 20 Pokémon By Speed")
    df = top_speed(pokemon_df)  
else:
    df = pokemon_df

# Show table
st.table(df)



