import streamlit as st

st.write("""
# Simple Stock Price Web App

Shown are the Stock Closing Price and Volume Of **Google**!

""")

import yfinance as yf



trackerSymbol="GOOGL"

trackerdata=yf.Ticker(trackerSymbol)


trackerDf=trackerdata.history(period="1d",start='2020-01-11',end='2022-01-11')




st.line_chart(trackerDf.Close)



st.line_chart(trackerDf.Volume)
