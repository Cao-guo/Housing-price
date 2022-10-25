import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data (1990) by Haoguo Cheng')
df = pd.read_csv('housing.csv')

## create a slider
Price_filter = st.slider('Median House Price', 0, 500001, 200000)
df = df[df.median_house_value <= Price_filter]

## create a multi select
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique()
)
df = df[df.ocean_proximity.isin(location_filter)]

## create a income select
income_filter = st.sidebar.radio(
    'Choose income level',
    ('low','median','high')
)
if income_filter == 'low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'median':
    df = df[(df.median_income > 2.5) & (df.median_income <= 4.5)]
elif income_filter == 'high':
    df = df[df.median_income > 4.5]

## show on map
st.markdown('###See more filters in the sidebar:')
st.map(df)

## show the histogram
st.markdown('###Histogram of the Median House Value:')
fig,ax = plt.subplots()
ax.hist(df.median_house_value, bins=30)
st.pyplot(fig)