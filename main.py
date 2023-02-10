

from extract import *
from functions import * 







if __name__ == '__main__':

	updateData()

	#for l in text:
	#print(l)


	data = pd.read_csv(dataFILE)

	print(data.head()) #Print the first rows

	print(len(data))

	drawMap(data)
	drawMap2(data)

