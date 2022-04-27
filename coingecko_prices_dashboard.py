# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:51:33 2022

@author: DKu_7
"""

# Obtain Top 200 Cryptos From Coingecko
# Imports

from bs4 import BeautifulSoup
import requests
import pandas as pd
import streamlit as st

# Obtain URL and get request:

url = "https://www.coingecko.com/"

response = requests.get(url)

# Initialize empty lists:

rank = []
name = []
ticker = []
price = []

change_1h = []
change_24h = []
change_7d = []
volume_24h = []
market_cap = []


# Obtain Top 300
for i in range(1, 4):
    
    # Website link with page number
    url = f'https://www.coingecko.com/?page={i}'
    
    # Request to website:
    response = requests.get(url)
    
    # Soup object:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Results from soup:
    results = soup.find('tbody').find_all('tr')
    
    # Append items:
    for result in results:
        # Rank, crypto name, ticker, price per unit:
        
        rank.append(result.find('td', {'class': 'table-number'}).get_text().strip())
        name.append(result.find('a', 
            {'class': 'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip() )
        ticker.append(result.find('a', {'class': 'd-lg-none font-bold tw-w-12'}).get_text().strip())
        price.append(result.find('span', {'class': 'no-wrap'}).get_text().strip())
        
        # % Changes, 24 hour volume and market cap:
        
        #change_1h.append(result.find('td', {'class': 'td-change1h'}).get_text().strip())
        change_24h.append(result.find('td', {'class': 'td-change24h'}).get_text().strip())
        change_7d.append(result.find('td', {'class': 'td-change7d'}).get_text().strip())
        #volume_24h.append(result.find('td', {'class': 'td-liquidity_score'}).get_text().strip())
        market_cap.append(result.find('td', {'class': 'td-market_cap'}).get_text().strip())
        
# Make as dataframe:

coingecko_df = pd.DataFrame({'Rank': rank, 'Crypto': name, 'Ticker': ticker,
                             'Price': price, '24h (%)': change_24h, 
                             '7d (%)': change_7d, 'Market Cap': market_cap})


## Frontend:
    
st.write("""
# Coingecko Top 300 Crypto Prices Dashboard
""")

st.write("""
         In this dashboard you can see the crypto prices webscraped by the Coingecko website. The table output below shows a
         portion of the full table. Click on the diagonal arrow at the top right to expand and see the full table.
""")

st.write(f"""
         Today's Date: {pd.to_datetime("today").strftime('%B %d %Y')} \n
         Time: {pd.to_datetime("today").strftime('%H:%M:%S')}
         """)

## Sidebar To Show Slider

values = st.sidebar.slider(
    'Select Range Of Ranks',
    1, 300, (1, 50)
 )



slider_df = coingecko_df.copy()

slider_df ['Rank'] = pd.to_numeric(slider_df ["Rank"])

slider_df = slider_df[(slider_df['Rank'] <= pd.to_numeric(values[1]))
                       & (slider_df['Rank'] >= pd.to_numeric(values[0]))]

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

# Show filtered dataframe in table:
st.table(slider_df)

## Sidebar To Show Top 5 Performing Cryptos In Last 7 Days:

# Sidebar table
    
df = coingecko_df.copy()
    
df['Rank'] = pd.to_numeric(df["Rank"])

df['7d (%)'] = df['7d (%)'].str.replace("%", "")
df['7d (%)'] = pd.to_numeric(df["7d (%)"]).round(1)

# Table Based On Choice
genre = st.sidebar.radio(
     "Choose Top 5 Or Bottom 5 Last 7 Days ",
     ('Top 5', 'Bottom 5'))

if genre == 'Top 5':
     side_table = df.sort_values("7d (%)", ascending = False).head(5)  
     st.sidebar.write("## Top 5 Cryptos Last 7 Days")
else:
     side_table = df.sort_values("7d (%)", ascending = True).head(5) 
     st.sidebar.write("## Bottom 5 Cryptos Last 7 Days")

st.sidebar.table(side_table[['Rank', 'Crypto', "7d (%)"]])

