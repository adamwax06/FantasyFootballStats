import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetches the web page to parse for data
page = requests.get('https://fantasydata.com/nfl/fantasy-football-leaders')

# Checks for connect(200 if successful)
print(page.status_code)

# Creates a bs4 soup object with the content of the html and the type of parser
soup = BeautifulSoup(page.content, 'html.parser')

# Finds the table inside the html file
table = soup.find('table', {'class': 'stats csv xls'})

# Keeps a list of all the rows omitting the first one
rows = table.find('tbody').find_all('tr')

# Creates an array to hold all players' data
players_data = []

# For loop to scrape the data we care about
for row in rows:
    cols = row.find_all('td')
    player_data = {
        'Name': cols[1].text.strip(),
        'Position': cols[3].text.strip(),
        'Fantasy Points PG': cols[17].text.strip(),
    }
    players_data.append(player_data)

# Creates a data frame(2D Array) and stores it in a csv
df = pd.DataFrame(players_data)
print(df)
df.to_csv('fantasy_top100.csv')