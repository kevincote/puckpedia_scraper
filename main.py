from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://puckpedia.com/e/players?e=p3e67d&sz=2000#&c=[2,3,4,5,7,10,12,15,17,19,20,21,22,23,24]"

w = requests.get(url)
soup = BeautifulSoup(w.content)

table = soup.find('table')

headers = [x.text for x in table.findAll('th')]
data_rows = table.find('tbody').findAll('tr')

df = pd.DataFrame(columns=headers)
for i, data_row in enumerate(data_rows):
  df.loc[i] = [x.text for x in data_row.findAll('td')]

df.to_csv('output.csv')

print('done')
