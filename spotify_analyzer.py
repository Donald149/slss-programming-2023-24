# Spotify Data Analyzer
# Author: Donald
# 16 January 2024

import csv

# Create a function that searches through data
# Finds all songs from a given artist


def find_all_songs(artist: str) -> list:
    """Searches through a set of data and 
    returns all songs found from a given artist

    Returns:
        A list found songs by given artist in tuples
        (artist, song name, danceability)
    """

    # Open
    with open("./spotify.csv") as f:
        # ----- Search for all artist Songs
        # ----- Use linear search
        # Create a csv reader object
        csv_reader = csv.DictReader(f)

        # Make a list to store all of artist's songs
        songs = []

        # Create a counter to store thee current line number
        line_num = 0

        # For every line in file
        for line in csv_reader:
            # First line -> print header
            if line_num == 0:
                # print("The columns are: ")

                # Print on one line:
                # print(", ".join(line))
                
                # Print one on every line
                # for item in line:
                    # print(item)
                
                line_num += 1
            else:
                # If the artist is who we looking for
                # Store the song info in the list
                # ----- artist, song title, danceability
                if artist.lower() in line["artist"].lower():
                    songs.append(
                        (line["artist"], line["song_title"], line["valence"], line["danceability"])
                    )
                line_num += 1

    return songs


drake_songs = find_all_songs("drake")
ed_sheeran_songs = find_all_songs("ed sheeran")

# Print the songs that have 
# a certain danceability or higher

# Starting at the beginning of the list until the end
for i, song in enumerate(drake_songs):
    # set the current item to the smallest danceability
    smallest_danceability = song[-1]
    smallest_idx = i
    
    # For the rest of the list
    for j in range(i +1, len(drake_songs)):
        # If the current item is smaller than the smallest
        if drake_songs[j][-1] < smallest_danceability:
            # set the smallest with the current
            smallest_danceability = drake_songs[j][-1]
            smallest_idx = j

    # swap the smallest with the current
    drake_songs[i], drake_songs[smallest_idx] = (
        drake_songs[smallest_idx], drake_songs[i]
    )

for songs in drake_songs:
    print(songs)

for i, song in enumerate(ed_sheeran_songs):
    # set the current item to the smallest danceability
    greatest_danceability = song[-1]
    greatest_idx = i
    
    # For the rest of the list
    for j in range(i +1, len(ed_sheeran_songs)):
        # If the current item is smaller than the smallest
        if ed_sheeran_songs[j][-1] < greatest_danceability:
            # set the smallest with the current
            greatest_danceability = ed_sheeran_songs[j][-1]
            greatest_idx = j

    # swap the smallest with the current
    ed_sheeran_songs[i], ed_sheeran_songs[greatest_idx] = (
        ed_sheeran_songs[greatest_idx],ed_sheeran_songs[i]
    )

for songs in ed_sheeran_songs:
    print(songs)