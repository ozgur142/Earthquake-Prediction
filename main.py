

from extract import *
from functions import * 
from ml import *





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
	groupLocation(data)

	# ********************** 
	#prediction model 
	print("prediction model 1")

	city = "Istanbul"
	coordinates = get_coordinates(city)

	filtered_data = pd.DataFrame(columns=data.columns)

	#updating data with only earthquake that closer than 150km
	for index, row in data.iterrows():
		# Calculate the distance between the two coordinates
		distance = coordsDistance(coordinates, (row['Latitude(N)'], row['Longitude(E)']))

		if distance < 150:
			# Add the row to the filtered DataFrame
			filtered_data = pd.concat([filtered_data, row.to_frame().T])


	print(filtered_data.head())
	
	#convert data to continius form to show that force = 0 when there is no seisim
	"""

	# Convert the time column to a datetime format
	df["time"] = pd.to_datetime(df["time"])

	# Set the time column as the index
	df = df.set_index("time")

	# Resample the data at a 1-minute frequency, using linear interpolation to fill in the missing values
	df = df.resample("1T").interpolate(method="linear")

	# Replace any remaining missing force values with 0
	df = df.fillna(0)

	"""
