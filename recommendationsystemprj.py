import random

# Sample movie data (replace with your dataset)
movies_data = {
    'arjun': ['Genre1', 'Director1'],
    'dasara': ['Genre2', 'Director2'],
    'murari': ['Genre1', 'Director3'],
    'sankranthi': ['Genre3', 'Director4'],
    'godfather': ['Genre2', 'Director5'],
    'darknight': ['Genre1', 'Director6'],
    'seven samuri': ['Genre3', 'Director7'],
    'citizen kane': ['Genre2', 'Director8'],
    'nayakan': ['Genre1', 'Director9'],
    'golmaal': ['Genre3', 'Director10']
}

# Sample user preferences (replace with actual user preferences)
user_preferences = ['Genre1', 'Genre2']

# Recommend movies based on user preferences
def recommend_movies(preferences, num_recommendations=5):
    recommended_movies = []
    for movie, details in movies_data.items():
        if details[0] in preferences:
            recommended_movies.append(movie)
    random.shuffle(recommended_movies)
    return recommended_movies[:num_recommendations]

# Get recommended movies for the user
recommended_movies = recommend_movies(user_preferences)

# Print recommended movies
print("Recommended movies for the user based on their preferences:")
for movie in recommended_movies:
    print(movie)
