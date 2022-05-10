# -*- coding: utf-8 -*-
"""
Created on Mon May  2 11:21:27 2022

@author: DKu_7
"""

# Crypto Price Plots

import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

## Sidebar Interface

st.subheader("Crypto Price Dashboard")

with st.sidebar:
    crypto_exchange = option_menu("Select A Crypto Exchange", 
                           ['Binance', "Kucoin", "Bitfinex",
                            "Gemini", "FTX"], default_index=0)


with st.expander("Info (Click To Expand)"):
    st.write("""
                     This dashboard allows the user to select a crypto pair from the left sideebar for its price plot. \n
                     
                     The user can choose an exchange and then a crypto pair below. \n
                     
                     Daily price data prices extracted from Cryptodatadownload.com. \n
                     
                     Crypto pairs can subject to change. 
                     """)

### Functions for obtaining data based on user selection

def get_bitfinex_link(crypto_pair):
    user_string = crypto_pair.replace("/", "")
    crypto_link = "https://www.cryptodatadownload.com/cdd/Bitfinex_" + user_string + "_d.csv"
    crypto_df = pd.read_csv(crypto_link, skiprows=[0])
    return(crypto_df)

def get_binance_link(crypto_pair):
    user_string = crypto_pair.replace("/", "")
    crypto_link = "https://www.cryptodatadownload.com/cdd/Binance_" + user_string + "_d.csv"
    crypto_df = pd.read_csv(crypto_link, skiprows=[0])
    return(crypto_df)

def get_kucoin_link(crypto_pair):
    user_string = crypto_pair.replace("/", "")
    crypto_link = "https://www.cryptodatadownload.com/cdd/Kucoin_" + user_string + "_d.csv"
    crypto_df = pd.read_csv(crypto_link, skiprows=[0])
    return(crypto_df)

def get_gemini_link(crypto_pair):
    user_string = crypto_pair.replace("/", "")
    crypto_link = "https://www.cryptodatadownload.com/cdd/Gemini_" + user_string + "_d.csv"
    crypto_df = pd.read_csv(crypto_link, skiprows=[0])
    return(crypto_df)

def get_ftx_link(crypto_pair):
    user_string = crypto_pair.replace("/", "")
    crypto_link = "https://www.cryptodatadownload.com/cdd/FTX_" + user_string + "_d.csv"
    crypto_df = pd.read_csv(crypto_link, skiprows=[0])
    return(crypto_df)


### Obtain data based on selected crypto pair:

if crypto_exchange == "Bitfinex":
    crypto_pair = st.selectbox(
         'Select A Crypto Ticker Pair:',
         ('ADA/USD', 'ALG/USD', 'AMP/USD', 'ANC/USD', 'APE/USD', 'AXS/USD', 'BAL/USD', 'BAT/USD', 
          'BNT/USD', 'BSV/USD', 'BTC/USD', 'CEL/USD', 'CHZ/USD', 'CRV/USD', 'DASH/USD', 'DGB/USD', 
          'DOT/USD', 'ENJ/USD', 'EOS/USD', 'ETC/USD',
          'ETH/USD', 'FET/USD', 'FIL/USD', 'FTM/USD', 'GRT/USD', 'ICP/USD', 'IQX/USD', 'JST/USD', 'KAI/USD',
          'KNC/USD', 'KSM/USD', 'LEO/USD', 'LRC/USD', 'LTC/USD', 'MIM/USD', 'MIR/USD', 'MKR/USD', 'MNA/USD',
          'NEO/USD', 'OMG/USD', 'PAX/USD', 'SNX/USD', 'SOL/USD', 'SRM/USD', 'TRX/USD', 'UNI/USD', 'UOS/USD',
          'UST/USD', 'VET/USD', 'WOO/USD', 'XDC/USD', 'XLM/USD', 'XMR/USD', 'XRP/USD', 'XTZ/USD', 'XVG/USD',
          'YFI/USD', 'ZEC/USD', 'ZIL/USD'))
    df = get_bitfinex_link(crypto_pair)
elif crypto_exchange == "Binance":
    # Select crypto pair (daily data)
    crypto_pair = st.selectbox(
         'Select A Crypto Ticker Pair:',
         ('AAVE/USDT', 'ADA/USDT', 'ALGO/USDT', 'AVAX/USDT', 'AXS/USDT', 'BAT/USDT', 'BNB/USDT', 'BTC/USDT',
          'BTT/USDT', 'CELR/USDT', 'COMP/USDT', 'CVC/USDT', 'DASH/USDT', 'DGB/USDT', 'DOGE/USDT',
          'DOT/USDT', 'EOS/USDT', 'ETC/USDT', 'ETH/USDT', 'FIL/USDT', 'ICP/USDT', 'ICX/USDT', 'IOTA/USDT',
          'LINK/USDT', 'LRC/USDT', 'LTC/USDT', 'LUNA/USDT', 'MATIC/USDT', 'MKR/USDT', 'NEAR/USDT', 'NEO/USDT',
          'ONE/USDT', 'ONT/USDT',  'QTUM/USDT', 'RVN/USDT', 'SC/USDT', 'SHIB/USDT', 'SOL/USDT',
          'STMX/USDT', 'STX/USDT', 'TRX/USDT', 'TUSD/USDT', 'UNI/USDT', 'USDC/USDT', 'VET/USDT', 'XLM/USDT',
          'XMR/USDT', 'XRP/USDT', 'XTZ/USDT', 'ZEC/USDT', 'ZIL/USDT'))
    df = get_binance_link(str(crypto_pair))
elif crypto_exchange == "Kucoin":
    crypto_pair = st.selectbox(
         'Select A Crypto Ticker Pair:',
         ('1INCH/USDT', 'AAVE/USDT', 'ADA/USDT', 'ALGO/USDT', 'ALICE/USDT', 'ALPACA/USDT', 'AMP/USDT', 
          'ANC/USDT', 'ANKR/USDT', 'APE/USDT', 'API3/USDT', 'AR/USDT', 'ARRR/USDT',
          'ATOM/USDT', 'AUDIO/USDT', 'AVAX/USDT', 'AXS/USDT', 'BAKE/USDT', 'BAL/USDT', 'BAND/USDT', 'BAT/USDT',
          'BCH/USDT', 'BEPRO/USDT', 'BNB/USDT', 'BNT/USDT', 'BTC/USDT', 'CAKE/USDT', 'CELO/USDT', 'CELR/USDT',
          'CHZ/USDT', 'CKB/USDT', 'CLV/USDT', 'COMP/USDT', 'COTI/USDT', 'CQT/USDT', 'CRO/USDT', 'CRV/USDT',
          'CTSI/USDT', 'CUDOS/USDT', 'DAG/USDT', 'DASH/USDT', 'DFI/USDT', 'DGB/USDT', 'DODO/USDT', 'DOGE/USDT',
          'DOT/USDT', 'EGLD/USDT', 'ENJ/USDT', 'ENS/USDT', 'EOS/USDT', 'ERG/USDT', 'ERSDL/USDT', 'ETC/USDT', 'ETH/USDT',
          'FIL/USDT', 'FLOW/USDT', 'FLUX/USDT', 'FTM/USDT', 'GHST/USDT', 'GRIN/USDT', 'HBAR/USDT',
          'HNT/USDT', 'HTR/USDT', 'HYDRA/USDT', 'ICP/USDT', 'ILV/USDT', 'IMX/USDT', 'INJ/USDT', 'IOTA/USDT', 
          'KAI/USDT', 'KAR/USDT', 'KAVA/USDT', 'KCS/USDT', 'KDA/USDT', 'KLAY/USDT', 'KNC/USDT', 'KP3R/USDT',
          'LINK/USDT', 'LPT/USDT', 'LRC/USDT', 'LTC/USDT', 'LUNA/USDT', 'MANA/USDT', 'MATIC/USDT', 'MIR/USDT',
          'MKR/USDT', 'MTV/USDT', 'NEAR/USDT', 'NEO/USDT', 'NOIA/USDT', 'OCEAN/USDT', 'OMG/USDT', 'OCEAN/USDT',
          'ONE/USDT', 'ONT/USDT', 'ORAI/USDT', 'PAXG/USDT', 'PRE/USDT', 'QNT/USDT', 'RFOX/USDT',  'RNDR/USDT', 'ROSE/USDT',
          'RUNE/USDT', 'SHIB/USDT', 'SNX/USDT', 'SOL/USDT', 'SRM/USDT', 'STMX/USDT', 'STORJ/USDT', 'SUSHI/USDT', 'SYS/USDT',
          'TEL/USDT', 'TFUEL/USDT', 'THETA/USDT', 'TONE/USDT', 'TRIAS/USDT', 'TRX/USDT', 'UNI/USDT',
          'UOS/USDT', 'USDC/USDT', 'VET/USDT', 'VRA/USDT', 'WAVES/USDT', 'WOO/USDT', 'XCAD/USDT',
          'XDC/USDT', 'XHV/USDT', 'XLM/USDT', 'XMR/USDT', 'XNO/USDT', 'XRP/USDT', 'YFI/USDT', 'ZEC/USDT', 'ZIL/USDT'))
    df = get_kucoin_link(str(crypto_pair))
elif crypto_exchange == "Gemini":
    crypto_pair= st.selectbox(
         'Select A Crypto Ticker Pair:',
         ('1INCH/USD', 'AAVE/USD', 'ALCX/USD', 'APEUSD', 'AUDIO/USD', 'AXS/USD','BAL/USD', 'BAT/USD', 
          'BCH/USD', 'BTC/USD', 'COMP/USD','CRV/USD', 'CTX/USD', 'DAI/USD', 'DOGE/USD', 
          'ENJ/USD', 'ENS/USD', 'ETH/USD', 'FTM/USD', 'FXS/USD', 'GALA/USD', 'GRT/USD', 'KNC/USD', 
          'LINK/USD', 'LRC/USD', 'LTC/USD', 'LUNA/USD', 'MANA/USD', 'MATIC/USD', 'MKR/USD', 'PAXG/USD', 
          'RAY/USD', 'REN/USD', 'RNDR/USD', 'SAND/USD', 'SHIB/USD', 'SNX/USD', 'SOL/USD', 'STORJ/USD', 
          'SUSHI/USD', 'UNI/USD', 'YFI/USD'))
    df = get_ftx_link(str(crypto_pair))
elif crypto_exchange == "FTX":
    crypto_pair= st.selectbox(
         'Select A Crypto Ticker Pair:',
         ('BTC/USDT', 'ETH/USDT', 'LTC/USDT', 'BNB/USDT', 'XRP/USDT', 'LINK/USDT', 'BCH/USDT', 'TRX/USDT'))
    df = get_ftx_link(str(crypto_pair))


#### Obtain dataframe based on user input:
# Skip first line with skiprows:

## Plot On Main Area
# Reference: https://discuss.streamlit.io/t/how-do-i-align-st-title/1668/13

fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

fig.update_layout(xaxis_title = "Date", 
                  yaxis_title = "Price",
                  height=600, width = 500,
                  title={
        'text': f"Daily Prices Line Plot of {crypto_pair} From {crypto_exchange}",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        font_size = 16)

st.plotly_chart(fig, use_container_width = True, height = 600, width = 500)
