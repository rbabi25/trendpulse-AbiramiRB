"""
TrendPulse - Task 2: Clean the Data & Save as CSV

Needs: data/trends_YYYYMMDD.json from Task 1

Produces: data/trends_clean.csv
"""

import glob
import pandas as pd


def find_latest_json_file():
    matching_files = glob.glob("data/trends_*.json")

    if not matching_files:
        print("No trends_*.json file found in data/. Run Task 1 first.")
        return None

    latest_file = sorted(matching_files)[-1]
    return latest_file


def load_data(filepath):
    """
    Task 1 (4 marks):
    Load the JSON file into a DataFrame and print the row count.
    """

    df = pd.read_json(filepath)

    print(f"Loaded {len(df)} stories from {filepath}")

    return df


def clean_data(df):
    """
    Task 2 (10 marks):
    Clean the DataFrame step by step.
    """

    # 1. Remove duplicate post_id rows
    df = df.drop_duplicates(subset="post_id")

    print(f"After removing duplicates: {len(df)}")

    # 2. Drop rows missing post_id, title, or score
    df = df.dropna(subset=["post_id", "title", "score"])

    print(f"After removing nulls: {len(df)}")

    # 3. Convert score and num_comments to integers
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # 4. Remove stories where score is less than 5
    df = df[df["score"] >= 5]

    print(f"After removing low scores: {len(df)}")

    # 5. Strip extra whitespace from title
    df["title"] = df["title"].str.strip()

    # Final cleaned row count
    print(f"After cleaning: {len(df)}")

    return df


def save_clean_csv(df, output_path="data/trends_clean.csv"):
    """
    Task 3 (6 marks):
    Save the cleaned DataFrame to CSV,
    print confirmation, and show category counts.
    """

    # Save cleaned DataFrame
    df.to_csv(output_path, index=False)

    # Confirmation
    print(f"Saved {len(df)} rows to {output_path}")

    # Category summary
    print("\nStories per category:")
    print(df["category"].value_counts())


def main():

    # Find latest JSON file
    filepath = find_latest_json_file()

    print("DEBUG filepath:", filepath)

    # Stop if no JSON file was found
    if filepath is None:
        return

    # Load JSON
    df = load_data(filepath)

    print("DEBUG df after load:")
    print(df)

    # Clean data
    df = clean_data(df)

    print("DEBUG df after clean:")
    print(df)

    # Save cleaned CSV
    save_clean_csv(df)


if __name__ == "__main__":
    main()