#Libraries
import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

#Page configuration
st.set_page_config(
    page_title="Cities",
    page_icon="cityscape",
    layout='wide'
)

#Data
df = pd.read_csv('zomato_final.csv')
image = Image.open('im.jpg')

#Sidebar
st.sidebar.image(image,width=300)
st.sidebar.markdown("# Zomato")
st.sidebar.markdown("""___""")
st.sidebar.markdown("## Filters")

#Filters
country_select = st.sidebar.multiselect("Select the countries to view their informations:",
                                        df['Country'].unique().tolist(),
                                        default=["Brazil", "Canada", "South Africa", "India", "Australia"])
df = df.loc[df['Country'].isin(country_select),:]

#Layout
st.write("# City Vision")

#Graphs
with st.container():
    df_aux = df.loc[:,['Restaurant ID','City','Country']].groupby(['Country','City']).count().sort_values('Restaurant ID',ascending=False).reset_index()
    fig = px.bar(df_aux.iloc[0:10,:],'City','Restaurant ID',text_auto=True, labels={'Restaurant ID':'Number of Restaurants','City':'Cities'}, color='Country')
    fig.update_layout(title_text='Top 10 Cities with More Restaurants Registered', title_x=0.3)
    st.plotly_chart(fig,use_container_width=True)
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        linhas_validas = df['Aggregate rating']>4
        df_aux = df.loc[linhas_validas,['Country','City','Restaurant ID']].groupby(['Country','City']).count().sort_values('Restaurant ID',ascending=False).reset_index()
        fig = px.bar(df_aux.iloc[0:5,:],'City','Restaurant ID',text_auto=True, labels={'Restaurant ID':'Number of Restaurants','City':'Cities'}, color='Country')
        fig.update_layout(title_text='Top 5 Cities With More Restaurants Rated Higher Than 4', title_x=0.1)
        st.plotly_chart(fig,use_container_width=True)
        
    with col2:
        linhas_validas = df['Aggregate rating']<2
        df_aux = df.loc[linhas_validas,['Country','City','Restaurant ID']].groupby(['Country','City']).count().sort_values('Restaurant ID',ascending=False).reset_index()
        fig = px.bar(df_aux.iloc[0:5,:],'City','Restaurant ID',text_auto=True, labels={'Restaurant ID':'Number Restaurants','City':'Cities'}, color='Country')
        fig.update_layout(title_text='Top 5 Cities With More Restaurants Rated Lower Than 2', title_x=0.1)
        st.plotly_chart(fig,use_container_width=True)
        
with st.container():
    df_aux = df.loc[:,['Country','City','Cuisines']].groupby(['Country','City']).nunique().sort_values('Cuisines',ascending=False).reset_index()
    fig = px.bar(df_aux.iloc[0:10,:],'City','Cuisines',text_auto=True, labels={'Cuisines':'Types of Cuisines','City':'Cities'}, color='Country')
    fig.update_layout(title_text='Top 10 Cities With More Types of Cuisines', title_x=0.4)
    st.plotly_chart(fig,use_container_width=True)