import pickle
from unicodedata import name
import streamlit as st
import requests
import pandas as pd
import random
from PIL import Image
import joblib

st. markdown("<h1 style='text-align: center; color: red;'>Movie Recommender</h1>", unsafe_allow_html=True)


image = Image.open('cinema3.jpg')
st.image(image, caption='Love Watching Movies')


def fetch_poster(movie_id):
    try :
        url = "https://api.themoviedb.org/3/movie/{}?api_key=42391464b98659f83cead58644f0eefb&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

    except:
        full_path = "" 

    return full_path

# Function will return list of [MOVIE POSTER] & [MOVIE NAME] of recommended movies based on Movie Name
def recommendByName(movie_title:str):
    new_df = pd.read_csv('movies.csv')
    genres_list='Action,Adventure,Fantasy,ScienceFiction,Crime,Drama,Thriller,Comedy,Romance,TVMovie,Documentary'


    if name  in enumerate(genres_list):
        contain_values = new_df[new_df['genres_list'].str.contains(name)]
        recommended_movie_names = contain_values['title'].tolist()
        recommended_movie_id = contain_values['movie_id'].tolist()
        for id_vector in recommended_movie_id:
            recommended_movie_posters.append(fetch_poster(movie_id))
        return recommended_movie_names,recommended_movie_posters

        

  
    index = movies[movies['title'] == movie_title].index[0]
    print(f"Index - {index}")
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    print(f"Distances - {distances}")
    recommended_movie_names = []
    recommended_movie_posters = []
    for id_vector in distances[1:15]:
        # fetch the movie poster
        movie_id = movies.iloc[id_vector[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[id_vector[0]].title)

    return recommended_movie_names,recommended_movie_posters

# Function will return list of [MOVIE POSTER] & [MOVIE NAME] of recommended movies based on Movie Genre
def recommendByGenre(movie_genre:str) :
    indexes, recommended_movie_names , recommended_movie_posters = [], [], []

    movies_list  = [movies.loc[index] for index in movies.index if str(movies['genres_list'][index]).find(movie_genre) != -1][:50]

    for i in range(14):
        index = random.randint(0, 50-1)

        # while loop incase the random index is already selected
        while indexes.count(index) >0:
            index = random.randint(0, 50-1)
        
        indexes.append(index)

        movie = movies_list[index]
        movie_id = movie.movie_id
        print(movie_id)
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movie.title)

    return recommended_movie_names,recommended_movie_posters

# Recommendation Option
options_list = ['Select recommendation type','Movie Name', 'Movie Genre']
option = st.selectbox(
     'How would you like to Search Movie?',
     options_list)

st.write('You selected:', option)

isSelectedByName = option == options_list[1]
isSelectedByGenre = option == options_list[2]

movies = pickle.load(open('movie_list.pkl','rb'))

# import zipfile

# with zipfile.ZipFile("similarity2.zip", 'r') as zip_ref:
#     zip_ref.extractall("new")

if isSelectedByName: 

    # similarity = pickle.load(open('test\similarity.pkl','rb'))
    similarity = joblib.load("mymodel.pkl")

    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

elif isSelectedByGenre:
    genres_list = joblib.load('genres.pkl')
    selected_genre = st.selectbox(
        'Type or select a genre from the dropdown',
        genres_list)

    st.write('You selected:', option)


def new_func(recommended_movie_names):
    st.text(recommended_movie_names[14])

if st.button('Show Recommendation'):
    if isSelectedByName:
        recommended_movie_names,recommended_movie_posters = recommendByName(selected_movie)
    elif isSelectedByGenre:
        recommended_movie_names,recommended_movie_posters =  recommendByGenre(selected_genre)

    print(recommended_movie_names)
    print(recommended_movie_posters)


    col1, col2 =st.columns(2)
    col3, col4 =st.columns(2)
    col5, col6 =st.columns(2)
    col7, col8 =st.columns(2)
    col9, col10 =st.columns(2)
    col11, col12 =st.columns(2)
    col13, col14 =st.columns(2)


    with col1:
        st.header(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])

    with col2:
        st.header(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.header(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])

    with col4:
        st.header(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])

    with col5:
        st.header(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

    with col6:
        st.header(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])

    with col7:
        st.header(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    
    with col8:
        st.header(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])

    with col9:
        st.header(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])

    with col10:
        st.header(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])

    with col11:
        st.header(recommended_movie_names[10])
        st.image(recommended_movie_posters[10])

    with col12:
        st.header(recommended_movie_names[11])
        st.image(recommended_movie_posters[11])

    with col13:
        st.header(recommended_movie_names[12])
        st.image(recommended_movie_posters[12])

    with col14:
        st.header(recommended_movie_names[13])
        st.image(recommended_movie_posters[13])    
        
