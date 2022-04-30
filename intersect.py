!pip install tmdbsimple
import tmdbsimple as tmdb
import requests

#Enter tmdb API key
api_key = ""
tmdb.API_KEY = api_key
search = tmdb.Search()

#Functions to scrape data
def get_id(movie):
  res = search.movie(query=movie)
  movie_id = res['results'][0]['id']
  return movie_id

def get_info(movie):
  id = get_id(movie)
  movie = tmdb.Movies(id)
  movie_info = movie.info()
  return movie_info

def get_credits(movie):
  id = get_id(movie)
  movie = tmdb.Movies(id)
  movie_info = movie.credits()
  return movie_info

def get_id_tv(tv):
  res = search.tv(query=tv)
  tv_id = res['results'][0]['id']
  return tv_id

def get_info_tv(tv):
  id = get_id_tv(tv)
  tv = tmdb.TV(id)
  tv_info = tv.info()
  return tv_info

def get_credits_tv(tv):
  id = get_id_tv(tv)
  url = "https://api.themoviedb.org/3/tv/"+str(id)+"/aggregate_credits?api_key="+api_key+"&language=en-US"
  response = requests.get(url)
  return response.json()

#Movie Intersect
input1 = input("Enter the first movie: ")
input2 = input("Enter the second movie: ")

data1 = get_credits(input1)['cast']
data2 = get_credits(input2)['cast']

main_cast1 = {x['name']:x['character'] for x in data1}
main_cast2 = {x['name']:x['character'] for x in data2}

intersect = set(main_cast1.keys()).intersection(set(main_cast2.keys()))

for i in intersect:
  print("--------------")
  print(i + " -> " + main_cast1[i])
  print(i + " -> " + main_cast2[i])
  print("--------------")


#TV Intersect
input1 = input("Enter the first show: ")
input2 = input("Enter the second show: ")

data1 = get_credits_tv(input1)['cast']
data2 = get_credits_tv(input2)['cast']

main_cast1 = {}
main_cast2 = {}

for i in range(len(data1)):
  main_cast1[data1[i]['name']] = data1[i]['roles'][0]['character']

for i in range(len(data2)):
  main_cast2[data2[i]['name']] = data2[i]['roles'][0]['character']

# main_cast1 = {x['name']:x['character'] for x in data1}
# main_cast2 = {x['name']:x['character'] for x in data2}

intersect = set(main_cast1.keys()).intersection(set(main_cast2.keys()))

for i in intersect:
  print("--------------")
  print(i + " -> " + main_cast1[i])
  print(i + " -> " + main_cast2[i])
  print("--------------")

#get_info_tv("The Boys Presents: Diabolical")