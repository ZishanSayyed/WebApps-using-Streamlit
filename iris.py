#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


# In[2]:


st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')


# In[3]:


def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features


# In[4]:


df = user_input_features()

st.subheader('User Input parameters')
st.write(df)


# In[5]:


iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)


# In[6]:


prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)


# In[7]:


st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)


# In[8]:


st.subheader('Prediction')
st.write(iris.target_names[prediction])


# In[9]:


#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)


# In[ ]:




