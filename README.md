[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/5GqajVEC)
# MSDS-597 Project

Group: [Insert Group Number]

## Project summary

Our project summary can be found:

- as a website:

https://ruiqi-qian.github.io/NBA/

## Accessing data

Our raw data can be downloaded here:

https://rutgers.box.com/s/2d8b2lxy0z238jw5ar5fafu6kysh9o9q

Our processed data can be downloaded here:

https://rutgers.box.com/s/yb6srg0fuck95u3ktjayzskzdecpqra5

NOTE: do not include your data in your git repo - it will likely be too large and cause issues.

## Python scripts / notebooks

The following scripts/notebooks were used produce the summary:

- `src/script.py`
- `notebooks/data_cleaning.ipynb`
- `notebooks/data_enrichment.ipynb`
- `notebooks/data_analysis.ipynb`

[Give a short description of what the notebooks contain, and their location in the git repo]

## Reproducibility

Provide a `requirements.txt` file with packages and versions of all python packages to run the analysis.

## Guide

### Summary

Your summary should include the following. 

Note: You do not need code in your summary - instead, reference where in your github repo the code is. The priority should be a concise, readable summary. You should include visualizations and conclusions regarding your data analysis.

1. describe where the data cam from, the format of the data, the nature of the data (e.g., what it contains, how often it is updated, etc). We get the 2 datasets from Kaggle and Github website.The first dataset examines NBA player performance across multiple seasons to determine key factors influencing salary. It includes attributes like points, assists, rebounds, net
rating, draft details, and accolades (https://www.kaggle.com/datasets/justinas/nba-players-data). The second datasetpresents the Salary of NBA players during the 2019-2024 season(https://github.com/madhurn1/PredictiveNBAContractValuationModel/blob/main/NBA%20Advanced%20Stats(2019%20-%202024).csv)

2. explain how you retrieved the data e.g. API, webscraping    We just download the data on the website

3. explain how you transformed raw data into tidy tabular data, including data cleaning Weloaded NBA player stats and salary data from 2019–2024.
We cleaned the data by:
Dropping missing values (e.g., in PER, TS%, salary, and position).
Standardizing column names (e.g., changing Player to player_name).
Selecting important columns like Season, Player, PER, TS%, Salary, and Position.
Splitting the data by season for easier processing.
Merging player stats with their position data, ensuring no missing positions.
At each stage, we saved cleaned datasets to CSV files, preparing tidy, analysis-ready data organized by season.

4. explain any tests you did to check data (e.g. using `pytest` to verify that no missing values are present in the tidied dataframes, verify that the resulting number of rows is reasonable)

5. explain any data enrichment steps

6. describe and explain meaningful summary statistics

7. present around 4-6 visualizations related to the data, explain trends and conclusions

You should have at least one interactive data widget.

You can include figures for example from an external notebook:
- https://quarto.org/docs/blog/posts/2023-03-17-jupyter-cell-embedding/ 
- https://quarto.org/docs/authoring/includes.html

8. at the end, display a graph of the git commit history

For team members of 2: 10 commits. Of 3: 15 commits. Of 4: 20 commits.

Your commits history elsewhere may be more dirty, but these 10-20 commits need to be clean and can be drawn as a graph.

Make sure your git graphs include author names, commit messages, date, git tags if any.

You can generate nice graphs of git commits with many tools. Among others, you could generate git-graphs using the following tools:

- in vscode: https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph
- https://stackoverflow.com/questions/1057564/pretty-git-branch-graphs
- https://www.gitkraken.com/solutions/commit-graph

### Data storage options

Some options for data storage:

- Box link (free with Rutgers account)
- Dropbox
- Google Drive

The following companies have free data storage (up to ~5 GB) for 12 months. Be careful to make sure you're within the free limits!!!

- AWS S3 https://aws.amazon.com/s3/
- Google Cloud https://cloud.google.com/free
- Microsoft Azure https://azure.microsoft.com/en-us/free/students

