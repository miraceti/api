import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# fonction qui definit la couleur des points sur la carte
def color_producer(elevation):
    ''' definition de la couleur des points par elevation'''
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
    
# carte centrée sur une zone
map = folium.Map(location=[38.58, -99.09], zoom_start=6)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(int(el))+"m",
    #icon = folium.Icon(color_producer(el))
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.7))

map.add_child(fgv)

map.save("Map01.html")
