import streamlit as st

st.write("""
# Simple Stock Price Web App

Shown are the Stock Closing Price and Volume Of **Google**!

""")

import yfinance as yf



tickerSymbol="GOOGL"

tickerData=yf.Ticker(tickerSymbol)


tickerDf=tickerData.history(period="1d",start='2020-01-11',end='2022-01-11')




st.line_chart(tickerDf.Close)



st.line_chart(tickerDf.Volume)
