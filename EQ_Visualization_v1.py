import pandas as pd
import numpy as np
import matplotlib
import seaborn
import folium
import requests # For acquiring data from URL
from bs4 import BeautifulSoup # For parsing data
import io

url = "http://www.koeri.boun.edu.tr/scripts/lst7.asp"
response = requests.get(url)
response.encoding = 'windows-1254'

#if response.status_code == 200: # Status code 200 means "OK"
    #print(response.text)
#else:
    #print(f"Failed to retrieve data. Status code: {response.status_code}")


html_content = response.text # Convert html data to string
soup = BeautifulSoup(html_content, 'html.parser') # Create a BeautifulSoup object
pre_tag = soup.find('pre')
data_text = pre_tag.get_text()
#print(data_text)


data_io = io.StringIO(data_text) # The below command expects a file-like object inside the brackets so we're converting the string data to file-like data.
df = pd.read_fwf (   # Convert fixed-width format to dataframe
    data_io,
    skiprows=[0, 1, 2, 3, 4, 6],
    header=0
)
#col_to_drop = [df.columns[i] for i in [5,7,9]] # This was a trial for removing the columns by indexes but received an error
#print(df.columns.tolist()) # This shows the exact names of every column. We used it to identify empty column names so we can put them inside the df.drop

df = df.drop(columns=['MD', 'Mw', 'Unnamed: 9']) # There were empty columns, we removed them here.
print(df)



