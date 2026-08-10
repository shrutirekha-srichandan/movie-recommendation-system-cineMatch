# movie-recommendation-system-cineMatch
# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using **Python, Pandas, NumPy, Scikit-learn, and Streamlit**. The system recommends movies similar to a movie selected by the user based on its content and metadata.

## 📌 Project Overview

This project uses a **content-based filtering** approach to recommend movies. Movie information such as **genres, keywords, cast, crew, and overview** is combined to create a single feature representation for each movie.

The **Bag of Words (BoW)** technique is then used to convert the textual features into numerical vectors. **Cosine Similarity** is applied to calculate the similarity between movies and generate the most relevant recommendations.

## 🚀 Features

* 🎥 Select a movie from the available movie list
* 🤖 Generate movie recommendations based on content similarity
* 🔤 Text feature extraction using **Bag of Words**
* 📊 Movie similarity calculation using **Cosine Similarity**
* 🌐 Interactive web interface using **Streamlit**
* ⭐ Displays the **Top 5 recommended movies**

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Pandas**
* **Scikit-learn**
* **Natural Language Processing (NLP)**
* **Bag of Words (CountVectorizer)**
* **Cosine Similarity**
* **Streamlit**

## ⚙️ How It Works

1. Load and preprocess the movie dataset using **Pandas**.
2. Combine relevant movie attributes such as genres, keywords, cast, crew, and overview.
3. Convert the combined text into numerical vectors using **CountVectorizer**.
4. Calculate similarity between movies using **Cosine Similarity**.
5. Find the movies with the highest similarity scores.
6. Display the **Top 5 similar movies** through the Streamlit application.

## 💻 Run Locally

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 🎯 Objective

The main objective of this project is to demonstrate how **machine learning and NLP techniques** can be used to build a practical recommendation system that suggests movies based on their content similarity.

## 📚 Concepts Learned

* Data preprocessing
* Feature engineering
* Natural Language Processing
* Text vectorization
* Bag of Words
* Cosine similarity
* Content-based recommendation
* Streamlit application development

