"""
TrendPulse - Task 3: Visualise the Data
----------------------------------------
Needs: data/trends_analysed.csv

Produces:
    outputs/chart1_top_stories.png
    outputs/chart2_categories.png
    outputs/chart3_scatter.png
    outputs/dashboard.png
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. SETUP
# ============================================================

# Load analysed data
df = pd.read_csv("data/trends_analysed.csv")

# Create outputs folder if it does not exist
os.makedirs("outputs", exist_ok=True)


# ============================================================
# 2. CHART 1 - TOP 10 STORIES BY SCORE
# ============================================================

# Select top 10 stories
top_stories = df.nlargest(10, "score").copy()

# Shorten titles longer than 50 characters
top_stories["short_title"] = top_stories["title"].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)

# Create horizontal bar chart
plt.figure(figsize=(10, 6))

plt.barh(
    top_stories["short_title"],
    top_stories["score"]
)

# Highest score at the top
plt.gca().invert_yaxis()

plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story Title")

plt.tight_layout()

# Save BEFORE show
plt.savefig("outputs/chart1_top_stories.png")

plt.show()

# Close figure
plt.close()


# ============================================================
# 3. CHART 2 - STORIES PER CATEGORY
# ============================================================

# Count stories in each category
category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))

# Different colour for each bar
plt.bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.tab10(range(len(category_counts)))
)

plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

plt.xticks(rotation=45)

plt.tight_layout()

# Save BEFORE show
plt.savefig("outputs/chart2_categories.png")

plt.show()

plt.close()


# ============================================================
# 4. CHART 3 - SCORE VS COMMENTS
# ============================================================

plt.figure(figsize=(9, 6))

# Popular stories
popular = df[df["is_popular"] == True]

# Non-popular stories
non_popular = df[df["is_popular"] == False]

# Plot popular stories
plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)

# Plot non-popular stories
plt.scatter(
    non_popular["score"],
    non_popular["num_comments"],
    label="Non-Popular"
)

plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")

plt.legend()

plt.tight_layout()

# Save BEFORE show
plt.savefig("outputs/chart3_scatter.png")

plt.show()

plt.close()


# ============================================================
# 5. BONUS - DASHBOARD
# ============================================================

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# ------------------------------------------------------------
# Dashboard Chart 1 - Top Stories
# ------------------------------------------------------------

axes[0].barh(
    top_stories["short_title"],
    top_stories["score"]
)

axes[0].invert_yaxis()

axes[0].set_title("Top 10 Stories by Score")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Story Title")


# ------------------------------------------------------------
# Dashboard Chart 2 - Categories
# ------------------------------------------------------------

axes[1].bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.tab10(range(len(category_counts)))
)

axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Number of Stories")

axes[1].tick_params(axis="x", rotation=45)


# ------------------------------------------------------------
# Dashboard Chart 3 - Scatter
# ------------------------------------------------------------

axes[2].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)

axes[2].scatter(
    non_popular["score"],
    non_popular["num_comments"],
    label="Non-Popular"
)

axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Number of Comments")

axes[2].legend()


# Overall dashboard title
fig.suptitle("TrendPulse Dashboard", fontsize=16)

plt.tight_layout()

# Save dashboard
plt.savefig("outputs/dashboard.png")

plt.show()

plt.close()


print("\nAll charts created successfully!")
print("Files saved in outputs/:")
print("- chart1_top_stories.png")
print("- chart2_categories.png")
print("- chart3_scatter.png")
print("- dashboard.png")