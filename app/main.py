import streamlit as st
import pickle
import pandas as pd
import requests

# Set page config for a more professional look
st.set_page_config(
    page_title="CineSphere | AI Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a premium, cinematic look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

    /* Main Background */
    .stApp {
        background: radial-gradient(circle at top right, #2d1b4e, #1a1a2e),
                    radial-gradient(circle at bottom left, #1a1a2e, #0f0c29);
        background-attachment: fixed;
        color: #ffffff;
        font-family: 'Outfit', sans-serif;
    }

    /* Typography */
    h1 {
        font-family: 'Outfit', sans-serif;
        font-weight: 800;
        font-size: 4rem !important;
        letter-spacing: -2px;
        background: linear-gradient(135deg, #FF0080 0%, #7928CA 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px !important;
        text-align: center;
        padding-top: 2rem;
    }
    
    .subtitle {
        font-size: 1.4rem;
        color: #b0b0d0;
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 300;
    }

    /* Movie Cards with Glassmorphism */
    .movie-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 15px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }

    .movie-card:hover {
        transform: translateY(-15px) scale(1.03);
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }

    .movie-title {
        font-weight: 600;
        margin-top: 15px;
        font-size: 1rem;
        color: #ffffff;
        min-height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        line-height: 1.2;
    }

    /* Poster Image */
    .movie-poster {
        width: 100%;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    }

    /* Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #FF0080 0%, #7928CA 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(121, 40, 202, 0.5);
        color: white;
    }

    /* Selectbox Styling */
    .stSelectbox label {
        color: #e0e0ff !important;
        font-size: 1.1rem !important;
    }
    
    div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px !important;
    }

    /* Hide Streamlit Header/Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

def fetch_poster(movie_id):
    try:
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f0f35825aa6b8803eae76a4af41a5421&language=en-US'.format(movie_id), timeout=5)
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        return "https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&q=80&w=500"
    except:
        return "https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&q=80&w=500"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    recommended_movie_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie, recommended_movie_poster

# Load data
@st.cache_resource
def load_data():
    try:
        movies_dict = pickle.load(open('models/movies_dict.pkl','rb'))
        movies = pd.DataFrame.from_dict(movies_dict)
        similarity = pickle.load(open('models/similarity.pkl','rb'))
    except FileNotFoundError:
        # Fallback for local development if running from within app folder
        movies_dict = pickle.load(open('../models/movies_dict.pkl','rb'))
        movies = pd.DataFrame.from_dict(movies_dict)
        similarity = pickle.load(open('../models/similarity.pkl','rb'))
    return movies, similarity

movies, similarity = load_data()

# Main UI
st.markdown("<h1>CineSphere</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Explore the universe of cinema. Discover your next favorite movie.</p>", unsafe_allow_html=True)

# Centered selection area
_, col_main, _ = st.columns([1, 2, 1])

with col_main:
    selected_movie_name = st.selectbox(
        'Search for a movie you enjoyed...',
        movies['title'].values
    )
    recommend_clicked = st.button('Unlock Recommendations')

if recommend_clicked:
    with st.spinner('✨ Deep diving into cinema history...'):
        names, posters = recommend(selected_movie_name)
        
        st.write("<div style='height: 40px;'></div>", unsafe_allow_html=True)
        cols = st.columns(5)
        
        for idx, col in enumerate(cols):
            with col:
                st.markdown(f"""
                <div class="movie-card">
                    <img src="{posters[idx]}" class="movie-poster">
                    <div class="movie-title">{names[idx]}</div>
                </div>
                """, unsafe_allow_html=True)

# Bottom info
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: rgba(255,255,255,0.4); font-size: 0.9rem; font-weight: 300;'>
    Using Cosine Similarity on TMDB 5000 Dataset<br>
    Crafted with ❤️ for Movie Lovers
</div>
""", unsafe_allow_html=True)
