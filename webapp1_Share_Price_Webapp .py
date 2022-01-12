#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system(' pip install streamlit')


# In[5]:


get_ipython().system('pip install yfinance')


# In[6]:


import streamlit as st
import yfinance as yf


# In[7]:


st.write("""
#Simple Stock Price Web App

Shown are the Stock Closing Price and Volume Of **Google**!

""")


# In[8]:


trackerSymbol="GOOGL"


# In[9]:


trackerdata=yf.Ticker(trackerSymbol)


# In[10]:


trackerDf=trackerdata.history(period="1d",start='2022-01-11',end='2022-01-11')


# In[11]:


st.line_chart(trackerDf.Close)


# In[12]:


st.line_chart(trackerDf.Volume)


# In[ ]:




