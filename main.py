import folium
from geopy.geocoders import Nominatim 

# Create map
my_map = folium.Map(location=[0.2983, 35.8035], zoom_start=500)

# Add OSM tile layer
folium.TileLayer(
    tiles='https://tile.openstreetmap.org/{z}/{x}/{y}.png',
    attr='Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors'
).add_to(my_map)

# Create geolocator 
geolocator = Nominatim(user_agent="my_application")

# Get location 
location = geolocator.geocode("Elburgon")

# Add marker
folium.Marker(
    [location.latitude, location.longitude], 
    popup=location.address
).add_to(my_map)

# Display map
my_map.save("my_map.html")