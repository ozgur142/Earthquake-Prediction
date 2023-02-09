
import geopandas as gpd
import matplotlib.pyplot as plt

def drawMap(df):
	fig, ax = plt.subplots(figsize=(8,6))
	countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

	countries[countries["name"] == "Turkey"].plot(color="lightgrey", ax=ax)

	df.plot(x="Longitude(E)", y="Latitude(N)", kind="scatter", colormap="YlOrRd", ax=ax)

	plt.show()
