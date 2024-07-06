import time
import csv
from jikanpy import Jikan
jikan = Jikan()

top_score = {}
top_pop = {}
images = {}

for yr in range(2000, 2025):
    anime = []

    szn = ["Winter", "Spring", "Summer", "Fall"]
    for s in szn:
        seasonal_anime = jikan.seasons(year=yr, season=s)

        for i in range(len(seasonal_anime['data'])):
            image_url = seasonal_anime['data'][i]['images']['jpg']['image_url']
            title = seasonal_anime['data'][i]['titles'][0]['title'].encode('ascii',errors='ignore').decode("utf-8")
            score = seasonal_anime['data'][i]['score']
            members = seasonal_anime['data'][i]['members']
            mal_id = seasonal_anime['data'][i]['mal_id']

            if score == None:
                continue

            anime.append([mal_id, score, members, image_url, title])
        
        time.sleep(1)

    top_score_this_year = sorted(anime, key=lambda x: x[1], reverse=True)[:5]
    top_pop_this_year = sorted(anime, key=lambda x: x[2], reverse=True)[:5]

    top_score[yr] = top_score_this_year
    top_pop[yr] = top_pop_this_year

fields = ["year", "top_score", "top_pop"]

with open('mal_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # writing headers (field names)
    writer.writerow(fields)

    for yr in range(2000, 2025):
        writer.writerow([yr, top_score[yr], top_pop[yr]])