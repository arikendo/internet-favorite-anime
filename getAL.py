import requests
import json
import csv
import time

popularity = '''
query getPopularity($startDate_greater: FuzzyDateInt, $startDate_lesser: FuzzyDateInt)
{
  Page (page: 1, perPage: 5) {
    pageInfo {
      total
      currentPage
      lastPage
      hasNextPage
      perPage
    }
    media(type: ANIME, startDate_greater: $startDate_greater, startDate_lesser: $startDate_lesser, sort: POPULARITY_DESC) {
      id
      title {
        romaji
      }
      popularity
      idMal
    }
  }
}
'''

score = '''
query getScore($startDate_greater: FuzzyDateInt, $startDate_lesser: FuzzyDateInt)
{
  Page (page: 1, perPage: 5) {
    pageInfo {
      total
      currentPage
      lastPage
      hasNextPage
      perPage
    }
   media(type: ANIME, startDate_greater: $startDate_greater, startDate_lesser: $startDate_lesser, sort: SCORE_DESC) {
      id
      title {
        romaji
      }
    	meanScore
      idMal
    }
}
}'''

url = 'https://graphql.anilist.co'

top_score = {}
top_pop = {}

yr = 2024

top_pop_this_year = []
top_score_this_year = []

variables = {
  'startDate_greater': yr*10000,
  'startDate_lesser': (yr+1)*10000
}

response = requests.post(url, json={'query': popularity, 'variables': variables})
pop = json.loads(response.content)

for index in range(0,5):
  # top_pop_this_year.append([pop['data']['Page']['media'][index]['title']['romaji'].encode('ascii',errors='ignore').decode("utf-8"), pop['data']['Page']['media'][index]['popularity']])
  top_pop_this_year.append([pop['data']['Page']['media'][index]['idMal'],
  pop['data']['Page']['media'][index]['popularity'], 
  pop['data']['Page']['media'][index]['title']['romaji'].encode('ascii',errors='ignore').decode("utf-8")
  ])

top_pop[yr] = top_pop_this_year


fields = ["year", "top_pop"]
with open('al_data_pop.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # writer.writerow(fields)
    writer.writerow([yr, top_pop[yr]])

    csvfile.close()