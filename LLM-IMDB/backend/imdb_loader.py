# imdb_loader.py

import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd

def load_imdb_data():
    file_path = "imdb_top_1000.csv"

    # Load dataset directly from KaggleHub
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows",
        file_path
    )

    # Combine important fields into a single "text" column for vector embeddings
    df["text"] = df.apply(
    lambda row: f"{row['Series_Title']} ({row['Released_Year']}) - Genre: {row['Genre']} - Rating: {row['IMDB_Rating']} - Overview: {row['Overview']} - Stars: {row['Star1']}, {row['Star2']}",
    axis=1
    )


    return df
