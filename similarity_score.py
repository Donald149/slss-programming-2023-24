# Comparing Similarity Scores
# Author: Donald
# 8 November 2023

# Calculate similarity scores between two people

# Create two lists that represents the movies that people like
ubials_favourite_movies = [
    "The Matrix",
    "Avengers: Infinity War",
    "The Empire Strikes Back",
    "Infernal Affairs",
    "Rogue One"
]

duck_favourite_movies = [
    "Your Name",
    "Infernal Affairs",
    "Avengers: Infinity War",
    "Weathering with you",
    "JJK 0"
]

# Inititalize the similarity score
similarity_score = 0

# Iterate through all movies in first list
for movie in ubials_favourite_movies:
    if movie in duck_favourite_movies:
        similarity_score += 1

# Display the results
print(f"Mr. Ubial and duck have a similarity score of: 2")