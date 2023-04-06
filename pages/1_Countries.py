#Libraries
import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

#Page configuration
st.set_page_config(
    page_title="Countries",
    page_icon="earth_americas",
    layout='wide'
)

#Leitura
df = pd.read_csv('zomato_final.csv')
image = Image.open('im.jpg')

#Barra
st.sidebar.image(image,width=300)
st.sidebar.markdown("# Zomato")
st.sidebar.markdown("""___""")
st.sidebar.markdown("## Filter")

#Filtros
country_select = st.sidebar.multiselect("Select the countries to view their informations:",
                                        df['Country'].unique().tolist(),
                                        default=["Brazil", "Canada", "South Africa", "India", "Australia"])

df = df.loc[df['Country'].isin(country_select),:]

#Layout
st.write("# Country Vision")

#Gráficos
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        df_aux = df.loc[:,['City','Country']].groupby('Country').nunique().sort_values('City',ascending=False).reset_index()
        fig = px.bar(df_aux,'Country','City',text_auto=True, labels={'City':'Number of Cities','Country':'Countries'})
        fig.update_layout(title_text='Cities Registered by Country', title_x=0.3)
        st.plotly_chart(fig,use_container_width=True)
    
    with col2:
        df_aux = df.loc[:,['Restaurant ID','Country']].groupby('Country').count().sort_values('Restaurant ID',ascending=False).reset_index()
        fig = px.bar(df_aux,'Country','Restaurant ID',text_auto=True, labels={'Restaurant ID':'Number of Restaurants','Country':'Countries'})
        fig.update_layout(title_text='Restaurants Registered by Country', title_x=0.3)
        st.plotly_chart(fig,use_container_width=True)
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        df_aux = df.loc[:,['Votes','Country']].groupby('Country').sum().sort_values('Votes',ascending=False).reset_index()
        fig = px.bar(df_aux,'Country','Votes',text_auto=True, labels={'Votes':'Number of Ratings Made','Country':'Countries'})
        fig.update_layout(title_text='Ratings Made by Country', title_x=0.3)
        st.plotly_chart(fig,use_container_width=True)
        
    with col2:
        df_aux = df.loc[:,['Aggregate rating','Country']].groupby('Country').mean().sort_values('Aggregate rating',ascending=False).reset_index()
        fig = px.bar(df_aux.round(2),'Country','Aggregate rating',text_auto=True, labels={'Aggregate rating':'Average Rating','Country':'Countries'})
        fig.update_layout(title_text='Average Rating by Country', title_x=0.4)
        st.plotly_chart(fig,use_container_width=True)
        
with st.container():
    df_aux = df.loc[:,['Country','Average Cost for two']].groupby('Country').mean().sort_values("Average Cost for two",ascending=False).reset_index()
    fig = px.bar(df_aux,'Country','Average Cost for two',text_auto=True, labels={'Average Cost for two':'Average Cost for Two (USD)','Country':'Country'})
    fig.update_layout(title_text='Average Cost of Dish for Two by Country', title_x=0.4)
    st.plotly_chart(fig,use_container_width=True)