
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
import math
import datetime
import numpy as np

def drawMap(df):
	fig, ax = plt.subplots(figsize=(8,6))
	countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

	countries[countries["name"] == "Turkey"].plot(color="lightgrey", ax=ax)

	df.plot(x="Longitude(E)", y="Latitude(N)", kind="scatter", colormap="YlOrRd", ax=ax)

	plt.show()


def drawMap2(data):
	# Create a map centered at the mean latitude and longitude of the data

	data = data.iloc[-100:]
	map_ = folium.Map(location=[39, 35], zoom_start=6.5)


	for index, d in data.iterrows():
		if d["ML"] > 4:
			folium.Marker(location=[d['Latitude(N)'], d['Longitude(E)']], popup=f"Time: {d[1]}, Depth(km): {d[4]},  Magnitude: {d[6]}", icon=folium.Icon(color="red", icon="info-sign")).add_to(map_)
		else:
			folium.Marker(location=[d['Latitude(N)'], d['Longitude(E)']], popup=f"Time: {d[1]}, Depth(km): {d[4]},  Magnitude: {d[6]}", icon=folium.Icon(color="green")).add_to(map_)

	# Show the map
	map_.save("map.html")



# calculating distance of 2 coordinates with Haversine formula
def coordsDistance(coord1, coord2):
	radius = 6371  # World diameter (km)
	lat1, lon1 = coord1
	lat2, lon2 = coord2
	dlat = math.radians(lat2 - lat1)
	dlon = math.radians(lon2 - lon1)
	a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
	     math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
	     math.sin(dlon / 2) * math.sin(dlon / 2))
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	distance = radius * c

	# Result
	print("Distance: {:.2f} km".format(distance))
	return distance


def date2float(dates):
	float_dates = []
	for date in dates.values:
		date = date[0]
		date_obj = datetime.datetime.strptime(date, "%Y.%m.%d")
		timestamp = datetime.datetime.timestamp(date_obj)
		float_date = float(timestamp)
		float_dates.append(float_date)
	return np.array(float_dates).reshape(-1, 1)

