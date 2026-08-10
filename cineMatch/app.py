import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies_list[movies_list['title']== movie].index[0]
    distances = similarity[movie_index]
    movies_similar = sorted(list(enumerate(distances)),reverse = True,key =lambda x:x[1])[1:6]
    
    recommend_movies = []
    for i in movies_similar:
        # movie_id =i[0]
        # fetch poster from API
        recommend_movies.append(movies_list.iloc[i[0]].title)
    return recommend_movies


movies_list = pickle.load(open('movies.pkl','rb'))
 

similarity = pickle.load(open('similarity_matrix.pkl','rb'))

st.title('cineMatch')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    (movies_list['title'].values),
)

st.write("You selected:", selected_movie_name)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)