# TrendPulse — HackerNews Trending Stories Analytics Pipeline

## 📌 Project Overview

TrendPulse is a Python-based data analytics project that collects trending stories from the HackerNews API, cleans and validates the data, performs statistical analysis, and generates visual insights.

The project demonstrates an end-to-end analytics workflow, transforming raw API data into structured datasets and decision-ready insights.

**Key highlights**
- Automated API data collection
- Rule-based story categorization across five categories
- Data cleaning, validation, and transformation
- Statistical analysis and KPI creation
- Data visualization and trend identification
- Error handling and GitHub version control

## 🎯 Project Objectives

- Collect trending stories from HackerNews.
- Categorize stories using title keywords.
- Improve data quality through cleaning and validation.
- Analyze story scores, comments, and engagement.
- Visualize category-level trends and top-performing stories.
- Build a reusable, multi-stage data processing pipeline.

## 🔄 Project Workflow

![TrendPulse Analysis Flowchart](images/trendpulse_flowchart.png)

**Pipeline:** Data Collection → Data Cleaning & Validation → Statistical Analysis & KPI Creation → Visualization → Insights

## 🛠️ Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python | Core programming and pipeline logic |
| Requests | API calls and data retrieval |
| JSON | Raw data storage |
| Time | Request delays |
| Pandas | Data cleaning, transformation, and analysis |
| NumPy | Statistical calculations |
| Matplotlib | Data visualization |
| Git & GitHub | Version control and code sharing |

## 📊 Project Tasks

### Task 1: Data Collection

- Retrieve story data using the HackerNews API.
- Combine Top Stories and New Stories IDs to improve coverage.
- Categorize stories into five groups using title keywords:
  - Technology
  - World News
  - Sports
  - Science
  - Entertainment
- Store selected story fields in a date-based JSON file.
- Handle request failures and continue processing where possible.

**Output:** `data/trends_YYYYMMDD.json`

**Milestone:** Successfully collected 112 stories in the initial completed version.

### Task 2: Data Cleaning & Validation

- Remove duplicate records.
- Handle missing and null values.
- Standardize data types.
- Remove stories with scores below 5.
- Strip unnecessary whitespace from titles.

**Output:** `data/trends_clean.csv`

### Task 3: Statistical Analysis & KPI Creation

Using Pandas and NumPy:

- Calculate mean, median, standard deviation, minimum, and maximum story scores.
- Identify the category with the highest number of stories.
- Find the most-commented story.
- Create an engagement metric.
- Derive an `is_popular` indicator using a defined rule.

**Output:** `data/trends_analysed.csv`

*Note: The engagement formula and popularity threshold should be documented in the code.*

### Task 4: Data Visualization

Using Matplotlib:

- Visualize top-performing stories.
- Compare story counts across categories.
- Present patterns that make trends easier to interpret.

**Planned outputs:**
- `outputs/chart1_top_stories.png`
- `outputs/chart2_categories.png`

## 🛡️ Data Quality & Error Handling

The pipeline incorporates practical data reliability measures:

- **Request failure handling:** Print an error message when a request fails and allow processing to continue where possible.
- **Duplicate removal:** Prevent repeated records from distorting analysis.
- **Missing-value handling:** Identify and remove records with missing required data.
- **Data type standardization:** Prepare fields for accurate calculations.
- **Business-rule filtering:** Exclude stories with scores below the specified threshold.

These controls help produce a more consistent dataset for analysis.

## 📈 Key Analytical Outputs

| Metric | Purpose |
|---|---|
| Mean and median score | Understand typical story performance |
| Standard deviation | Measure variation in story scores |
| Minimum and maximum score | Identify the score range |
| Story count by category | Compare category distribution |
| Most-commented story | Identify discussion activity |
| Engagement metric | Measure interaction using the defined formula |
| Popularity indicator | Flag stories meeting the defined threshold |

## 💼 Business & FP&A Relevance

Although TrendPulse uses public news data rather than financial statements, the analytical methods are transferable to finance and business reporting.

- **KPI and trend analysis:** Monitor business performance indicators.
- **Data validation:** Improve the reliability of financial reporting inputs.
- **Exception identification:** Flag records that fail defined business rules.
- **Process automation:** Reduce repetitive manual data preparation.
- **Decision support:** Convert raw data into clear visual insights.

**Potential FP&A applications:** Budget vs Actuals, forecasting, variance analysis, revenue and cost trends, and management reporting.

## 🤖 AI/ML Usage

This version is a **data analytics project, not an AI/ML project**.

- Story categorization uses keyword-based rules.
- Statistical analysis uses Pandas and NumPy.
- No machine learning model or generative AI model is trained or integrated.

Future enhancements could include NLP-based story classification, engagement prediction, and anomaly detection.

## 📁 Project Structure

```text
trendpulse/
├── task1_data_collection.py
├── task2_data_processing.py
├── task3_data_analysis.py
├── task4_visualization.py
├── data/
│   ├── trends_YYYYMMDD.json
│   ├── trends_clean.csv
│   └── trends_analysed.csv
├── outputs/
│   ├── chart1_top_stories.png
│   └── chart2_categories.png
├── images/
│   └── trendpulse_flowchart.png
├── .gitignore
└── README.md
```

*Adjust filenames to match the actual files in your repository. Generated data files may remain local if excluded through `.gitignore`.*

## ⚙️ Setup & Execution

### 1. Clone the repository

```bash
git clone https://github.com/<username>/trendpulse-<name>.git
cd trendpulse-<name>
```

### 2. Install dependencies

```bash
pip install requests pandas numpy matplotlib
```

### 3. Run the pipeline

Execute the scripts in sequence, after confirming the actual filenames and paths:

```bash
python task1_data_collection.py
python task2_data_processing.py
python task3_data_analysis.py
python task4_visualization.py
```

Each stage depends on the output generated by the preceding stage.

## 🚀 Key Learnings

- Working with REST APIs and JSON data.
- Implementing data cleaning and validation rules.
- Performing statistical analysis using Pandas and NumPy.
- Creating analytical metrics and visualizations.
- Handling request failures and improving processing reliability.
- Managing project code with Git and GitHub.

## 📌 Project Status

- **Task 1 — Data Collection:** Completed; 112 stories collected in the initial successful run.
- **Task 2 — Data Cleaning:** In progress.
- **Task 3 — Statistical Analysis:** Pending implementation.
- **Task 4 — Visualization:** Pending implementation.

Status should be updated as each stage is completed and tested.

## 👤 Author

Python | Data Analytics | Business & Finance Analytics

GitHub: https://github.com/rbabi25/trendpulse-AbiramiRB/blob/main/task1_data_collection.py
https://github.com/rbabi25/trendpulse-AbiramiRB/blob/main/task2_data_processing.py
https://github.com/rbabi25/trendpulse-AbiramiRB/blob/main/task3_analysis.py
https://github.com/rbabi25/trendpulse-AbiramiRB/blob/main/task4_visualization.py


