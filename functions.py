
import geopandas as gpd
import matplotlib.pyplot as plt
import folium

def drawMap(df):
	fig, ax = plt.subplots(figsize=(8,6))
	countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

	countries[countries["name"] == "Turkey"].plot(color="lightgrey", ax=ax)

	df.plot(x="Longitude(E)", y="Latitude(N)", kind="scatter", colormap="YlOrRd", ax=ax)

	plt.show()


def drawMap2(data):
	# Create a map centered at the mean latitude and longitude of the data

	map_ = folium.Map(location=[39, 35], zoom_start=6.5)


	for index, d in data.iterrows():
		if d["ML"] > 4:
			folium.Marker(location=[d['Latitude(N)'], d['Longitude(E)']], popup=f"Time: {d[1]}, Location: {d[7]}", icon=folium.Icon(color="red", icon="info-sign")).add_to(map_)
		else:
			folium.Marker(location=[d['Latitude(N)'], d['Longitude(E)']], popup=f"Time: {d[1]}, Location: {d[7]}", icon=folium.Icon(color="green")).add_to(map_)

	# Show the map
	map_.save("map.html")
