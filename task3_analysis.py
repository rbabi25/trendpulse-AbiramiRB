"""
TrendPulse - Task 3: Analyse the Data with Pandas & NumPy
------------------------------------------------------------
Needs: data/trends_clean.csv from Task 2
Produces: data/trends_analysed.csv
"""

import pandas as pd
import numpy as np


def load_and_explore(filepath="data/trends_clean.csv"):
    """
    Task 1 (4 marks):
      - Load the CSV
      - Print first 5 rows
      - Print shape
      - Print average score and average num_comments
    """

    df = pd.read_csv(filepath)

    print("Loaded data:")
    print(df.head())

    print("\nShape:", df.shape)

    print("\nAverage score:", round(df["score"].mean(), 2))
    print("Average num_comments:", round(df["num_comments"].mean(), 2))

    return df


def numpy_stats(df):
    """
    Task 2 (8 marks): Use NumPy for statistics.
    """

    # Mean, median, standard deviation
    mean_score = np.mean(df["score"])
    median_score = np.median(df["score"])
    std_score = np.std(df["score"])

    # Maximum and minimum
    max_score = np.max(df["score"])
    min_score = np.min(df["score"])

    # Category with most stories
    category_counts = df["category"].value_counts()
    top_category = category_counts.idxmax()
    top_category_count = category_counts.max()

    # Story with most comments
    max_comments_index = df["num_comments"].idxmax()
    top_story = df.loc[max_comments_index, "title"]
    top_story_comments = df.loc[max_comments_index, "num_comments"]

    print("\n--- NumPy Statistics ---")
    print("Mean score:", round(mean_score, 2))
    print("Median score:", round(median_score, 2))
    print("Standard deviation:", round(std_score, 2))
    print("Maximum score:", max_score)
    print("Minimum score:", min_score)

    print("\nCategory with most stories:")
    print(top_category, "-", top_category_count)

    print("\nStory with most comments:")
    print(top_story, "-", top_story_comments)


def add_columns(df):
    """
    Task 3 (5 marks): Add 'engagement' and 'is_popular' columns.

    engagement = score + num_comments
    is_popular = score >= 100
    """

    df["engagement"] = df["score"] + df["num_comments"]

    df["is_popular"] = df["score"] >= 100

    return df


def save_result(df, output_path="data/trends_analysed.csv"):
    """
    Task 4 (3 marks): Save and confirm.
    """

    df.to_csv(output_path, index=False)

    print("\nAnalysis complete!")
    print("Saved analysed data to:", output_path)


def main():
    df = load_and_explore()
    numpy_stats(df)
    df = add_columns(df)
    save_result(df)


if __name__ == "__main__":
    main()