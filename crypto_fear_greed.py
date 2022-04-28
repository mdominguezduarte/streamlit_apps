# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:52:21 2022

@author: DKu_7
"""

import requests
import pandas as pd
import streamlit as st
import datetime
import plotly.express as px

st.write("""
# Cryptocurrency Fear & Greed Index
""")


with st.expander("Fear & Greed Index Info (Click to Expand)"):
     st.write("""
         The crypto fear and greed index shows the market sentiment in the cryptocurrency market space. 

         Fear is where the index value is below 50 and above 0. This could be a good time to buy.

         Greed is where the index value is above 50 and less than 100. Many expect prices to go even higher. This could be a good time to take profits & sell.

     """)

# Reference my own jupyter notebook: https://github.com/dk81/crypto_python/blob/main/feargreed_stockscrypto.ipynb
# Url for Crypto Fear & Greed Index:
url = "https://api.alternative.me/fng/?limit=0"

# Making a get request
response = requests.get(url)

#### Dataframe & data cleaning items:
# Crypto fear and greed data into a dataframe:
fg_crypto_df = pd.DataFrame(response.json()['data'])

# Change timestamp values into dates:
fg_crypto_df['timestamp'] = pd.to_datetime(fg_crypto_df['timestamp'], unit="s")

# Change column names:
fg_crypto_df.columns = ['Value', 'Label', 'Date', 'Time Until Update']

# Change value into a numeric column:
fg_crypto_df['Value'] = pd.to_numeric(fg_crypto_df['Value'])

## Date choice on sidebar
date = st.sidebar.date_input('Select Start Date For Plot', datetime.date(2018,2,1))

# Today's date:
today_date = date.today()

# Filter by date choice
if date > date.today():
    st.write("**Error: Selected date is past today's date. Please choose another date.**")
else:
    df = fg_crypto_df[fg_crypto_df.Date > date.strftime("%Y-%m-%d")]

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


## Today's Crypto Fear & Greed Index Value

### Plot & Table

# Sidebar Colour picker:

pick_color = st.sidebar.color_picker(label = "Plot Colour", value = "#286EE0")


side_df = df.copy()

side_df['Date'] = pd.to_datetime(side_df['Date']).dt.date

side_df.set_index("Date")

st.sidebar.title("Last 5 Days - Crypto Fear & Greed Index")

st.sidebar.table(side_df.head()[['Date', 'Value', 'Label']])

## Plot On Main Area

colT1,colT2 = st.columns([1,8])
with colT2:
    st.title("Crpyto Fear & Greed Plot")

fig = px.line(df, x="Date", y="Value")
fig.update_traces(line_color= pick_color)

st.plotly_chart(fig, use_container_width = True, height = 300, width = 300)
