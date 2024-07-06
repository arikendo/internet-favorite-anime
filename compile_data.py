import csv
import json

MAL_scores = {}
MAL_pop = {}

with open('mal_data.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        if lines[0] == "year":
            continue

        year = lines[0]
        pop_data = lines[2].split(',')
        score_data = lines[1].split(',')

        pop_clean = []
        score_clean = []

        for i in range(0,len(pop_data)-5,5):
            arr = []

            name = str(pop_data[i+4].strip("[] [ ] ' ' "))
            mal_id = str(pop_data[i].strip("[] [ ] ' ' "))
            popularity = int(pop_data[i+2].strip(' '))
            image_url = str(pop_data[i+3].strip("[] [ ]  ' ' "))
            
            arr = [mal_id, popularity, image_url, name]

            pop_clean.append(arr)

        for i in range(0,len(score_data)-5,5):
            arr = []

            name = str(score_data[i+4].strip("[] [ ] ' ' "))
            mal_id = str(score_data[i].strip("[] [ ] ' ' "))
            score = float(score_data[i+1].strip(' '))
            image_url = str(score_data[i+3].strip("[] [ ]  ' ' "))
            
            arr = [mal_id, score, image_url, name]

            score_clean.append(arr)
        MAL_pop[year] = pop_clean
        MAL_scores[year] = score_clean

AL_pop = {}

with open('al_data_pop.csv', mode='r') as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        if lines[0] == "year":
            continue

        year = lines[0]
        pop_data = lines[1].split(',')

        pop_clean = []

        for i in range(0,len(pop_data),3):
            arr = []

            mal_id = str(pop_data[i].strip("[] [ ] ' ' "))
            name = str(pop_data[i+2].strip("[] [ ] ' ' "))
            popularity = int(pop_data[i+1].strip(' [ ] '))
            
            arr = [mal_id, popularity, name]

            pop_clean.append(arr)
        
        AL_pop[year] = pop_clean

AL_scores = {}

with open('al_data_score.csv', mode='r') as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        if lines[0] == "year":
            continue

        year = lines[0]
        score_data = lines[1].split(',')

        score_clean = []

        for i in range(0,len(score_data),3):
            arr = []

            mal_id = str(score_data[i].strip("[] [ ] ' ' "))
            name = str(score_data[i+2].strip("[] [ ] ' ' "))
            score = int(score_data[i+1].strip(' [ ] '))
            
            arr = [mal_id, score, name]

            score_clean.append(arr)
        
        AL_scores[year] = score_clean

top_score_every_year = {}
top_pop_every_year = {}

for yr in range(2000, 2025):
    year = str(yr)
    current_year = []

    MAL_pop_current_year = MAL_pop[year]
    AL_pop_current_year = AL_pop[year]

    for mal_anime in MAL_pop_current_year:
        for al_anime in AL_pop_current_year:
            if mal_anime[0] == al_anime[0]:
                current_year.append([mal_anime[0], mal_anime[3], mal_anime[1]+al_anime[1], mal_anime[2]])

    top_pop_every_year[yr] = sorted(current_year, key=lambda x: x[2], reverse=True)[:3]

    current_year = []

    MAL_score_current_year = MAL_scores[year]
    AL_score_current_year = AL_scores[year]

    for mal_anime in MAL_score_current_year:
        for al_anime in AL_score_current_year:
            if mal_anime[0] == al_anime[0]:
                current_year.append([mal_anime[0], mal_anime[3], final_score, mal_anime[2]])
    
    top_score_every_year[yr] = sorted(current_year, key=lambda x: x[2], reverse=True)[:1][0]

print(top_score_every_year)
# print(top_pop_every_year)

with open("score.json", "w") as json_file:
    json.dump(top_score_every_year, json_file)

# with open("popularity.json", "w") as json_file:
#     json.dump(top_pop_every_year, json_file)