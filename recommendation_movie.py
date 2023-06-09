# -*- coding: utf-8 -*-
"""Recommendation Movie

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LEgar8Vcx8GWy9XqxM7ZzVdXUy694NMv
"""

import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv('/content/movies.csv')

movies.head()

movies.shape

selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
print(selected_features)

for features in selected_features:
  movies[features] = movies[features].fillna('')

combined = movies['genres']+' '+movies['keywords']+' '+movies['tagline']+' '+movies['cast']+' '+movies['director']

print(combined)

vector = TfidfVectorizer()

feature_vector = vector.fit_transform(combined)

print(feature_vector)

similar = cosine_similarity(feature_vector)

print(similar)

print(similar.shape)

moviename = input('Enter the movie name :')

titles = movies['title'].tolist()
print(titles)

close_match = difflib.get_close_matches(moviename, titles)
if close_match:
  print(close_match)
else:
  print("no data")

find_match = close_match[0]
print(find_match)

index = movies[movies.title == find_match]['index'].values[0]
print(index)

score = list(enumerate(similar[index]))
print(score)

similar_movies = sorted(score , key = lambda x:x[1], reverse = True)
print(similar_movies)

i = 1
for m in similar_movies:
  index_no = m[0]
  title = movies[movies.index == index_no]['title'].values[0]
  if (i< 11):
    print(i , '-',title)
    i+=1

"""COMBINING ALL THE ABOVE CODES AND WROTE DOWN BELOW, IT IS THE SAME CODE AS ABOVE ONLY THING IS WE ARE COMBINING IT IN ONE OVERALL CODE

"""

movies = pd.read_csv('/content/movies.csv')


selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

for features in selected_features:
  movies[features] = movies[features].fillna('')

combined = movies['genres']+' '+movies['keywords']+' '+movies['tagline']+' '+movies['cast']+' '+movies['director']

vector = TfidfVectorizer()

feature_vector = vector.fit_transform(combined)

similar = cosine_similarity(feature_vector)

moviename = input('Enter the movie name :')

titles = movies['title'].tolist()

close_match = difflib.get_close_matches(moviename, titles) 
if close_match:
  print('movie found')
else:
  print('movie not found in database') 

find_match = close_match[0]

index = movies[movies.title == find_match]['index'].values[0]

score = list(enumerate(similar[index]))

similar_movies = sorted(score , key = lambda x:x[1], reverse = True)

i = 1 
for m in similar_movies:
  index_no = m[0]
  title = movies[movies.index == index_no]['title'].values[0]
  if (i< 11):
    print(i , '-',title)
    i+=1