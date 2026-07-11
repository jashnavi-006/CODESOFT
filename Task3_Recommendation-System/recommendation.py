import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("movies.csv")

# Convert genres into vectors
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["Genre"])

# Calculate similarity
similarity = cosine_similarity(genre_matrix)

def recommend(movie_name):
    movie_name = movie_name.lower()

    if movie_name not in movies["Movie"].str.lower().values:
        print("Movie not found!")
        return

    index = movies[movies["Movie"].str.lower() == movie_name].index[0]

    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    count = 0
    for i, score in scores:
        if i != index:
            print(movies.iloc[i]["Movie"])
            count += 1
        if count == 5:
            break

while True:
    movie = input("\nEnter a movie name (or type 'exit'): ")

    if movie.lower() == "exit":
        print("Thank you for using the Movie Recommendation System!")
        break

    recommend(movie)