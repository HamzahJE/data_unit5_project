import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.title('Unit 5 Project - Admin Dashboard')

DATA_URL=r'supermarket.csv'


@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")
data.store_id.astype(str)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data,use_container_width=True)

st.title('Total Sales')
total_sales=data.store_sales.sum()
st.success(f'### {total_sales}')

st.title('Total Customers')
total_customers=data.daily_customer_count.sum()
st.success(f'### {total_customers}')



st.title('Top 10 Selling stores ')
top_selling=data.sort_values(by='store_sales',ascending=False).drop(columns=['store_area','items_available','daily_customer_count']).iloc[:10,:]
top_selling.store_id=top_selling.store_id.astype(str)
if st.checkbox('View Highest 10 Selling Stores as a Data Table'):
    st.subheader('Data Table')
    st.write(top_selling)

# st.bar_chart(data=top_selling,y='store_sales',x='store_id')
fig_top=px.bar(top_selling,y='store_sales',x='store_id')
st.plotly_chart(fig_top)

st.title('Lowest 10 Selling stores ')
low_selling=data.sort_values(by='store_sales',ascending=True).drop(columns=['store_area','items_available','daily_customer_count']).iloc[:10,:]
low_selling.store_id=low_selling.store_id.astype(str)
if st.checkbox('View Lowest 10 Selling Stores as a Data Table'):
    st.subheader('Data Table')
    st.write(low_selling)

# st.bar_chart(data=low_selling,y='store_sales',x='store_id')
fig_low=px.bar(low_selling,y='store_sales',x='store_id')
st.plotly_chart(fig_low)