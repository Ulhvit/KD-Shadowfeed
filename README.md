# KD-Shadowfeed

KD-Shadowfeed is a personal YouTube data engineering (and analysis) project that extracts patterns from YouTube watch history using Python and SQLite.
It demonstrates skills in data engineering(database creation and management) and HTML parsing.

The project's name sounds more ominous than intended for some reason. 
Shadow is the data footprint I casted over the years of YouTube usage.
Feed is for feeding that shadow into the code to analyze it.
I do not claim to be good at naming stuff.

## Features

- Parses YouTube watch history to extract video links, titles, channels and timestamps.
- Stores processed data in a SQLite database.
- Optimized for memory-efficient parsing using generators and memory clears where applicable.
- TO DO: analyze trends and viewing habits.

## Privacy

This repository **does not include any personal YouTube history**. All code is designed to work with local data files that remain private.  
For demonstration purposes, the repo will include **synthetic sample data** (`example.db`) that mirrors the structure of the real data.

## TODO

I step: Process the data and create a database (~20% done)
II step: Prepare example database for demonstration purposes 
III step: Plan approach to data analysis
IV step: Analyze the data
V step: Prepare example data visualization graphics for demonstration purposes

