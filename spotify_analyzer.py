# Spotify Data Analyzer
# Author: Donald
# 16 January 2024

import csv

# Open
with open("./spotify.csv") as f:
    # ----- Search  for all Drake Songs
    # ----- Use linear search
    # Create a csv reader object
    csv_reader = csv.DictReader(f)

    # Make a list to store all of Drake's songs
    drake_songs = []

    # Create a counter to store thee current line number
    line_num = 0

    # For every line in file
    for line in csv_reader:
        # First line -> print header
        if line_num == 0:
            print("The columns are: ")

            # Print on one line:
            print(", ".join(line))
            
            # Print one on every line
            # for item in line:
                # print(item)
            
            line_num += 1
        else:
            # If the artist is who we looking for
            # Store the song info in the list
            # ----- artist, song title, dancability
            if "drake" in line['artist'].lower():
                drake_songs.append((
                    line['artist'],
                    line['song_title'],
                    line['danceability']
                ))
            line_num += 1

    for song in drake_songs:
        if float(song[-1]) > 0.5:
            print(song)