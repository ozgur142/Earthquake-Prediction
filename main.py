

from extract import *
from functions import * 

from sklearn.cluster import KMeans




if __name__ == '__main__':

	data = pd.read_csv(dataFILE)

	print("nomber of data: ", len(data))

	updateData()

	#data = pd.read_csv(dataFILE, header=None)
	data = pd.read_csv(dataFILE)

	print(data.head()) #Print the first rows

	print("nomber of data: ", len(data))

	drawMap(data)
	drawMap2(data)

	#a = date2float(data.loc[:, ["Date"]])
	X = data.loc[:, ["Latitude(N)", "Longitude(E)"]].values

	#kmeans to group coordinates of earthquakes
	kmeans = KMeans(n_clusters=20)
	kmeans.fit(X)

	# Kümelerin etiketlerinin tahmin edilmesi
	labels = kmeans.predict(X)

	# Verilerin görselleştirilmesi
	plt.scatter(X[:, 1], X[:, 0], c=labels)
	plt.show()

	#polynomial regression

