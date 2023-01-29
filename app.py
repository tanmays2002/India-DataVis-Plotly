import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df= pd.read_csv('India.csv')
list_of_state = list(df.State.unique())
list_of_state.insert(0,'Overall India')

st.set_page_config(layout='wide')
st.sidebar.title('India ka Data Visualization')
selected_state = st.sidebar.selectbox('Select a State',list_of_state)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))
plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represent Primary parameter')
    st.text('color represent Secondary parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat=df['Latitude'], lon=df['Longitude'], zoom=4,size_max=35,
                               size=primary,color=secondary, mapbox_style="carto-positron",
                                width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df, lat=state_df['Latitude'], lon=state_df['Longitude'], zoom=4, size_max=35,
                                size=primary, color=secondary, mapbox_style="carto-positron",
                                width=1200, height=700,hover_name="District")
        st.plotly_chart(fig, use_container_width=True)



