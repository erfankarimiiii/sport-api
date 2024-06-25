import requests
import json
import asyncio

print ("A. Laliga(2023-2024)")
print ("B. Premier Leauge(2023-2024)")
print ("C. SerieA(2023-2024) ")
user_input = input ("Pls Choose a Player (A , B , C) : ")
if user_input == "B" or user_input == "b" :
       api_key = 'bb960424cbed4beca0834bf04e37164e'  

       leagues = ['PD', 'BL1', 'PL', 'FL1', 'SA']  

       for league in leagues:
          url = f'https://api.football-data.org/v2/competitions/{league}/matches'
          headers = {'X-Auth-Token': api_key}

          response = requests.get(url, headers=headers)

          if response.status_code == 200:
             matches = response.json()['matches']
             print(f'\n Live results of the French league {league}:')
             for match in matches:
               home_team = match['homeTeam']['name']
               away_team = match['awayTeam']['name']
               result = f"{home_team} {match['score']['fullTime']['homeTeam']} - {match['score']['fullTime']['awayTeam']} {away_team}"
               print(result) 
          else:
            print('No live games found.')
else:
          print(f'Error getting league information{league}.')