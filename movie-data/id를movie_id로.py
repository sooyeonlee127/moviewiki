import json
from collections import OrderedDict




movie_json = open('./movie-data/genres.json', encoding='utf-8') # 불러오는 파일
movie_dict = json.load(movie_json)
result = []
for movie in movie_dict:
  inner_dict = dict()
  inner_dict["model"] = "movies.genre"
  inner_dict["fields"] = movie
  result.append(inner_dict)


with open('./genres_1.json', 'w', encoding='utf-8') as file: # 저장하는 파일
  json.dump(result, file, ensure_ascii=False, indent=4)
