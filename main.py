

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

	#polynomial regression

