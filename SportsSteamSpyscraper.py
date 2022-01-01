from bs4 import BeautifulSoup
import requests 
import pandas as pd

url = 'https://steamspy.com/genre/Sports'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
  
data = []
table = soup.find('table', attrs={'id':'gamesbygenre'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
    
df = pd.DataFrame(data)
df.columns=['#', 'title', 'releasedate', 'price', 'Score_rank', 'owners', 'playtime_median', 'developers', 'publishers' ]

df.to_csv('../Thesis/Sportssteamspy.csv', index = False, encoding='utf-8')
print('Succesfully saved!') 