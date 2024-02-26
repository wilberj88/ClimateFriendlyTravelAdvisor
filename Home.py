import streamlit as st
import googlemaps
from datetime import datetime
from ipywidgets import embed
import streamlit.components.v1 as components



st.title("🌎 Climate Friendly Travel Advisor📍")
st.header("By Wilber Jiménez Hernández")

def new_york():

    # Plot coordinates
    coordinates = (40.75, -74)
    _map = gmaps.figure(center=coordinates, zoom_level=12)

    # Render map in Streamlit
    snippet = embed.embed_snippet(views=_map)
    html = embed.html_template.format(title="", snippet=snippet)
    return components.html(html, height=500,width=500)

new_york()
snippet = embed.embed_snippet(views=map)
html = embed.html_template.format(title="", snippet=snippet)
components.html(html, height=500,width=500)


api_key1 = st.secrets["GOOGLEMAPS_API_KEY"]

gmaps = googlemaps.Client(key=api_key1)


# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)
