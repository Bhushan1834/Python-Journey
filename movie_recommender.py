import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load the Movie Dataset
# Using a common public dataset URL for content-based filtering
url = "https://raw.githubusercontent.com/codeheroku/Introduction-to-Machine-Learning/master/Building%20a%20Movie%20Recommendation%20Engine/movie_dataset.csv"
try:
    df = pd.read_csv(url)
    print("Movie dataset loaded successfully.\n")
except:
    # Minimal synthetic dataset if URL fails
    print("URL failed. Creating a synthetic movie dataset for demonstration...")
    data = {
        'index': [0, 1, 2, 3, 4],
        'title': ['Avatar', 'Star Wars', 'The Dark Knight', 'Inception', 'The Avengers'],
        'genres': ['Action Adventure Fantasy', 'Action Adventure Sci-Fi', 'Action Crime Drama', 'Action Sci-Fi Thriller', 'Action Adventure Sci-Fi'],
        'cast': ['Sam Worthington', 'Mark Hamill', 'Christian Bale', 'Leonardo DiCaprio', 'Robert Downey Jr'],
        'keywords': ['future culture clash', 'reproduction space war', 'dc comics joker', 'dream submarine', 'marvel comic superhero'],
        'director': ['James Cameron', 'George Lucas', 'Christopher Nolan', 'Christopher Nolan', 'Joss Whedon']
    }
    df = pd.DataFrame(data)

# 2. Select and Clean Features
features = ['keywords', 'cast', 'genres', 'director']

# Filling NaNs with empty string
for feature in features:
    df[feature] = df[feature].fillna('')

def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']

# Applying feature combination
df["combined_features"] = df.apply(combine_features, axis=1)

print("Sample combined features string:")
print(df["combined_features"].head(1).values[0])
print("\n")

# 3. Vectorization using CountVectorizer
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])

# 4. Compute Cosine Similarity
similarity_scores = cosine_similarity(count_matrix)

# 5. Recommendation Logic
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    try:
        return df[df.title == title]["index"].values[0]
    except:
        return None

def recommend_movies(movie_user_likes, n=5):
    movie_index = get_index_from_title(movie_user_likes)
    
    if movie_index is None:
        print(f"Movie '{movie_user_likes}' not found in dataset.")
        return

    # Get scores for this movie
    similar_movies = list(enumerate(similarity_scores[movie_index]))

    # Sort movies by similarity score
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

    print(f"Movies similar to '{movie_user_likes}':")
    i = 0
    for movie in sorted_similar_movies:
        if i == 0: # Skip the movie itself
            i += 1
            continue
        print(f"{i}. {get_title_from_index(movie[0])}")
        i += 1
        if i > n:
            break

# 6. Test the Recommender
recommend_movies("Avatar")
print("\n")
recommend_movies("Star Wars")
