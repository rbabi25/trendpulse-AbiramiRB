"""
TrendPulse - Task 2: Clean the Data & Save as CSV
---------------------------------------------------
SKELETON FILE - fill in the TODOs yourself.
This is a scaffold to guide your own implementation, not a finished script.

Needs: data/trends_YYYYMMDD.json from Task 1
Produces: data/trends_clean.csv
"""

import glob
import pandas as pd


def find_latest_json_file():
    """
    Find the most recent trends_*.json file in the data/ folder,
    so you don't have to hardcode a specific date in the filename.
    Hint: glob.glob("data/trends_*.json") gives you a list of matching paths.
    Hint: sorted(...)[-1] gives you the last one alphabetically, which
    for YYYYMMDD-formatted dates is also the most recent one.
    """
    # TODO: implement this
    pass


def load_data(filepath):
    """
    Task 1 (4 marks): Load the JSON file into a DataFrame and print the row count.
    """
    # TODO: use pd.read_json() to load the file
    # TODO: print("Loaded {N} stories from {filepath}")
    pass


def clean_data(df):
    """
    Task 2 (10 marks): Clean the DataFrame step by step.
    Print the row count after EACH stage, in this order:
      1. Remove duplicate post_id rows      -> print("After removing duplicates: {N}")
      2. Drop rows missing post_id/title/score -> print("After removing nulls: {N}")
      3. Convert score & num_comments to int
      4. Remove rows where score < 5        -> print("After removing low scores: {N}")
      5. Strip whitespace from title

      Think about WHY steps 2 and 3 are in that specific order before you code it.
    """
    # TODO: step 1 - drop_duplicates on post_id

    # TODO: step 2 - dropna on post_id, title, score

    # TODO: step 3 - astype(int) on score and num_comments

    # TODO: step 4 - filter where score >= 5

    # TODO: step 5 - strip whitespace on title

    return df


def save_clean_csv(df, output_path="data/trends_clean.csv"):
    """
    Task 3 (6 marks): Save to CSV, print a confirmation, and print a
    per-category breakdown.
    """
    # TODO: df.to_csv(...)
    # TODO: print("Saved {N} rows to {output_path}")
    # TODO: print category counts using value_counts()
    pass


def main():
    filepath = find_latest_json_file()
    df = load_data(filepath)
    df = clean_data(df)
    save_clean_csv(df)


if __name__ == "__main__":
    main()
