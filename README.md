![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/-Docker-333333?style=flat&logo=docker)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)

# MLOps Project for Steam Platform

Individual Project for 'Soy Henry' Data Boot Camp

## Project Description

In this project, we simulate the role of an MLOps Engineer, combining responsibilities of a Data Engineer and Data Scientist, for the multinational video game platform, Steam. The goal is to develop a Minimum Viable Product (MVP) that includes a deployed API in a cloud service and the application of two Machine Learning models. These models address sentiment analysis on user comments about games and game recommendations based on user information.

Steam is a digital distribution platform for video games, it has over 325 million users and offers more than 25,000 games in its catalog.

## Used Datasets

Three provided JSON files were used:

1. `australian_user_reviews.json`: Contains user comments on games, recommendation information, emoticons, and statistics. It also includes the user ID, profile URL, and game ID.

2. `australian_users_items.json`: Provides information about games played by users and the cumulative time played by each user on a specific game.

3. `output_steam_games.json`: Contains data related to games, such as title, developer, prices, and technical features.

## Transformations and Feature Engineering

- Extraction, Transformation, and Loading (ETL) were performed using the Pandas library.
- Strategies were applied to handle nested data, and irrelevant or highly null columns were removed.
- The 'sentiment_analysis' column was created to classify comments as negative, neutral, or positive using TextBlob.
- Auxiliary dataframes were generated to optimize API performance and were saved in parquet format for storage efficiency.

## Exploratory Data Analysis (EDA)

- EDA was conducted on transformed datasets using Pandas, Matplotlib, and Seaborn.
- Relevant variables for creating the recommendation model were identified.

## Recommendation Models

- Two recommendation models were developed: item-item and user-game.
- Memory-based algorithms were used, utilizing cosine similarity to measure similarities between games and users.
- Lists of 5 recommended games were generated for a specific game or user, respectively.

This README provides an overview of the MLOps project for the Steam platform, highlighting key processes and outcomes. For detailed information on implementation, refer to the documentation and source code on the [GitHub repository](https://github.com/leocortes85/PI_MLOps_Steam). You can also access the API and explore the documentation at the [API link](/docs).

To learn more about the creator of this project, visit his [LinkedIn profile](https://www.linkedin.com/in/leonardo-cort%C3%A9s-zambrano-13522295/)(LinkedIn" src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin).

