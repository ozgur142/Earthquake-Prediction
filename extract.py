import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os

dataFILE = 'earthquake_data.csv'
url = 'http://www.koeri.boun.edu.tr/scripts/lst8.asp'

def convertData(data):
    data = data.split("\n")[7:]
    for line in range(len(data)):
        data[line] = data[line].split()[:9]

    data = [e for e in data if e != []]

    for line in data:
        line[2] = float(line[2])
        line[3] = float(line[3])
        line[4] = float(line[4])
        line[5] = None if line[5] == "-.-" else float(line[5])
        line[6] = None if line[6] == "-.-" else float(line[6])
        line[7] = None if line[7] == "-.-" else float(line[7])

    return data

def updateData():
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the table on the page
        text = soup.find('pre').text
        

        data = convertData(text)

        if not (os.path.exists(dataFILE)):
            header = ['Date', 'Time', 'Latitude(N)', 'Longitude(E)', 'Depth(km)', 'MD', 'ML', 'Mw', 'Location']
            # write the list to a csv file
            with open(dataFILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(data)

        else:
            updating(data)

    else:
        print('Failed to retrieve data from the website')



#TODO ******** TODO ***** TODO ***** TODO
def updating(data):
    print("file is updating...")




    














"""
    body = soup.find('body', class_='page page-id-60 page-child parent-pageid-58 page-template page-template-template-onecolumn page-template-template-onecolumn-php mobile')
    div1 = body.find('div', class_='hfeed')
    div2 = div1.find('div', id='main')
    div3 = div2.find('div', id='forbottom')
    section1 = div3.find('section', id='container')
    div4 = section1.find('div', id='content')
    div5 = div4.find('div', id='post-60')
    div6 = div5.find('div', class_='entry-content')
    p1 = div6.find('p')
    """