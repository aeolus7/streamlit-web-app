import pandas as pd
import streamlit as st
import plotly_express as px
from st_aggrid import AgGrid, grid_options_builder
st.set_page_config(page_title="Evolution Bitcoin",
                   page_icon=":bar_chart:",
                   layout="wide",
                   initial_sidebar_state="collapsed")
df = pd.read_csv("C:/Users/waila/Desktop/BTC-USD.csv")
AgGrid(df, editable=True,
       width=900,
       theme="material",
       )

chart = px.line(df, x='Date', y='Volume', title='evolution de bitcoin par le temps', markers=True, line_shape='hvh')
chart.update_layout(
    autosize=True,
    width=1500,
    height=750,),
paper_bgcolor = "LightSteelBlue",
#st.plotly_chart(chart)
x1 = st.date_input("entrer la date")
st.write(x1)
#y=df.loc[df['Volume']._where(df['Date'] == x1)]
df2 = df.loc[df['Date'] == str(x1), 'Volume']
st.write(df2)
