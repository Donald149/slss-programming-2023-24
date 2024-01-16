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
                # ----- artist, song title, dancability
                if artist.lower() in line["artist"].lower():
                    songs.append(
                        (line["artist"], line["song_title"], line["danceability"])
                    )
                line_num += 1

    return songs


drake_songs = find_all_songs("drake")
ed_sheeran_songs = find_all_songs("ed sheeran")

# Print the songs that have 
# a certain dancibility or higher

for song in ed_sheeran_songs:
    if float(song[-1]) > 0.5:
        print(song)