<div align="center">

# 🍿 CineSphere
**Your Personal AI Movie Matchmaker**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movie-recommender-system-a.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

<img src="https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&q=80&w=1000" alt="CineSphere Header" style="border-radius: 15px; margin-top: 15px; margin-bottom: 15px;">

**[Try the Live App Here!](https://movie-recommender-system-a.streamlit.app/)** 👈

</div>

---

## 💡 About The Project

Ever finished a great movie and wondered, *"What should I watch next?"* 

**CineSphere** is an intelligent, content-based recommendation system that solves exactly that. By analyzing the deep metadata of over 5,000 films (including genres, keywords, cast, and crew), it maps out the cinematic universe and finds hidden gems that perfectly match your taste.

It's not just a script; it's a fully interactive web application wrapped in a premium, glassmorphic UI.

---

## ⚡ Features

- **🧠 Smart AI Engine**: Uses machine learning and Cosine Similarity to find the 5 closest movie matches out of a massive 5,000-dimensional vector space.
- **🖼️ Real-Time Posters**: Automatically fetches high-quality movie posters on the fly using the TMDB API.
- **🚀 Cloud-Optimized**: Implements `.pbz2` compression to handle massive similarity matrices seamlessly on cloud platforms like Streamlit Community Cloud.
- **✨ Premium Design**: A custom CSS dark-mode interface designed to feel like a high-end streaming service.

---

## 🛠️ Built With

*   **Frontend**: [Streamlit](https://streamlit.io/)
*   **Data Manipulation**: [Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)
*   **Machine Learning**: [Scikit-Learn](https://scikit-learn.org/) *(CountVectorizer, Cosine Similarity)*
*   **Data Source**: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) & [TMDB API](https://developer.themoviedb.org/docs)

---

## ⚙️ How It Works (Under the Hood)

1.  **Data Ingestion**: We merge movie metadata with cast & crew credits.
2.  **Feature Engineering**: We extract the top 3 actors, the director, genres, and descriptive keywords.
3.  **Text Processing**: Everything is combined into a massive text "tag". We remove common stop words and normalize the text.
4.  **Vectorization**: The tags are fed into a `CountVectorizer` to create a 5000-feature mathematical representation of every movie.
5.  **Distance Calculation**: We calculate the *Cosine Similarity* (the angle between vectors) to find which movies are mathematically closest to each other.

---

## 💻 Run It Locally

Want to spin this up on your own machine? It's easy!

### 1. Clone & Install
```bash
git clone https://github.com/Ashu4495/Movie-Recommender-System.git
cd Movie-Recommender-System
pip install -r requirements.txt
```

### 2. Generate the Brain (The ML Models)
Run our script to process the data, train the vectors, and generate the highly-compressed `.pbz2` similarity matrix.
```bash
python scripts/generate_similarity.py
```

### 3. Launch the App
```bash
streamlit run app/main.py
```
*Your browser will automatically open to `http://localhost:8501`*

---

<div align="center">
    <b>Crafted with ❤️ for Movie Lovers</b>
</div>
