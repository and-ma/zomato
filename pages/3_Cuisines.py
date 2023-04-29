#Bibliotecas
import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

#Page configuration
st.set_page_config(
    page_title="Cuisines",
    page_icon="cook",
    layout='wide'
)

#Helper function
def best(nat):
    df2 = pd.read_csv("zomato_final.csv")
    df_aux = df2.loc[df2['Cuisines']==nat,:]
    df_aux.sort_values('Aggregate rating',ascending=False).reset_index()
    rating = df_aux['Aggregate rating'].iloc[1]
    name = df_aux['Restaurant Name'].iloc[0]
    return st.markdown("{}: {}  \n ### {}/5.0".format(nat, name, rating))

#Leitura
df = pd.read_csv('zomato_final.csv')
image = Image.open('im.jpg')

#Barra
st.sidebar.image(image,width=300)
st.sidebar.markdown("# Zomato")
st.sidebar.markdown("""___""")
st.sidebar.markdown("## Filters")

#Filtros
country_select = st.sidebar.multiselect("Select the countries to view their informations:",
                                        df['Country'].unique().tolist(),
                                        default=["Canada", "India"])
df = df.loc[df['Country'].isin(country_select),:]
st.sidebar.markdown("""___""")
cuisine_select = st.sidebar.multiselect("Select the types of cuisines to view:",
                                        df['Cuisines'].unique().tolist(),
                                        default=["Canadian", "Indian"])
df = df.loc[df['Cuisines'].isin(cuisine_select),:]
st.sidebar.markdown("""___""")
num_slider = st.sidebar.slider("Select the number of restaurants you would like to view",
                                  value=10, min_value=1, max_value=50)

df_aux = df.loc[:,['Restaurant Name','Country','City','Cuisines','Aggregate rating','Average Cost for two']].sort_values("Aggregate rating", ascending=False).reset_index()
df_aux = df_aux.iloc[:num_slider,:]

#Layout
st.write("# Vision Cuisine")

with st.container():
    st.markdown("## Best Restaurants of the Main Types of Cuisines")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        best('Brazilian')
        
    with col2:
        best('American')
        
    with col3:
        best("Italian")
        
    with col4:
        best("Japanese")
        
    with col5:
        best("Chinese")

with st.container():
    st.markdown("## Top {} Restaurants".format(num_slider))
    df_aux

with st.container():
    col1, col2 = st.columns(2)
    df2 = pd.read_csv("zomato_final.csv")
    
    with col1:
        df_aux = df2.loc[:,['Cuisines','Aggregate rating']].groupby('Cuisines').mean().sort_values('Aggregate rating',ascending=False).reset_index()
        fig = px.bar(df_aux.iloc[0:num_slider,:],'Cuisines','Aggregate rating',text_auto=True, labels={'Aggregate rating':'Average Ratings','Cuisines':'Types of cuisines'})
        fig.update_layout(title_text='The Top {} Types of Cuisines With the Best Ratings'.format(num_slider), title_x=0.3)
        st.plotly_chart(fig,use_container_width=True)    
   
    with col2:
        df_aux = df2.loc[:,['Cuisines','Aggregate rating']].groupby('Cuisines').mean().sort_values('Aggregate rating',ascending=True).reset_index()
        fig = px.bar(df_aux.iloc[0:num_slider,:],'Cuisines','Aggregate rating',text_auto=True, labels={'Aggregate rating':'Average Ratings','Cuisines':'Types of Cuisines'})
        fig.update_layout(title_text='The Top {} Types of Cuisines With the Worst Ratings'.format(num_slider), title_x=0.3)
        st.plotly_chart(fig,use_container_width=True)
