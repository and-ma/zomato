#Libraries
import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import pandas as pd
from PIL import Image

#Page configuration
st.set_page_config(
    page_title="Home Page",
    page_icon="house",
    layout='wide'
)

#Importing
df = pd.read_csv('zomato_final.csv')
image = Image.open('im.jpg')

#Sidebar
st.sidebar.image(image,width=300)
st.sidebar.markdown("# Zomato")
st.sidebar.markdown("""___""")

#Layout
st.write("# Zomato!")
st.markdown("## Global Platform Information")

#Data
restaurants = df['Restaurant ID'].nunique()
countries = df['Country'].nunique()
cities = df['City'].nunique()
ratings = df['Votes'].sum()
cuisines = df['Cuisines'].nunique()

#Metrics
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        col1.metric("Registered Restaurants", restaurants)

    with col2:
        st.metric("Registered Countries", countries)

    with col3:
        st.metric("Registered Cities", cities)

    with col4:
        st.metric("Ratings Made", ratings)

    with col5:
        st.metric("Types of Cuisines", cuisines)

#Map    
with st.container():
    map = folium.Map(zoom_start=11)
    marker_cluster = MarkerCluster().add_to(map)
    for index, location in df.iterrows():
        folium.Marker([location['Latitude'],
                      location['Longitude']],
                     icon = folium.Icon(icon="icon",color=df['Rating Color'].tolist()[index])).add_to(marker_cluster)
    folium_static(map,1024,600)