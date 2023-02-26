from sklearn.cluster import KMeans

import matplotlib.pyplot as plt

def groupLocation(data):
	X = data.loc[:, ["Latitude(N)", "Longitude(E)"]].values

	#kmeans to group coordinates of earthquakes
	kmeans = KMeans(n_clusters=80)
	kmeans.fit(X)

	# Kümelerin etiketlerinin tahmin edilmesi
	labels = kmeans.predict(X)

	# Verilerin görselleştirilmesi
	plt.scatter(X[:, 1], X[:, 0], c=labels)
	plt.show()