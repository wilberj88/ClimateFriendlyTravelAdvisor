import streamlit as st

#GoogleMapsApiRouteKey=AIzaSyDBgNgcuFP8Swarp8gfR-PxLM8-Wm90774

import googlemaps
from datetime import datetime



st.title("🌎 Climate Friendly Travel Advisor📍")
st.header("By Wilber Jiménez Hernández")


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
