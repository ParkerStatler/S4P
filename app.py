import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.title('US Vehicle Information')

v_df = pd.read_csv('../vehicles_us_cleaned.csv')

st.write(v_df)

st.subheader('Number of cars for each manufacturer')
fig = px.histogram(v_df, x="model")
st.plotly_chart(fig)


x_axis = st.selectbox('X axis', df.columns, index=1)
y_axis = st.selectbox('Y axis', df.columns, index=2)
color = st.selectbox('Color', df.columns, index=3)
st.subheader(f'Scatter plot matrix of {x_axis} and {y_axis} by {color}')
fig = px.scatter_matrix(df, dimensions=[x_axis, y_axis], color=color)
st.plotly_chart(fig)
