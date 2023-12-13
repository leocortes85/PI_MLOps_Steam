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

In this project, we simulate the role of an MLOps Engineer, combining responsibilities of a Data Engineer and Data Scientist, for the multinational video game platform, Steam. The goal is to develop a Minimum Viable Product (MVP) that includes a deployed API in a cloud service and the application of two Machine Learning models. These models address sentiment analysis on user comments about games, game recommendations based on user information and the similarity between games by genre.

Steam is a digital distribution platform for video games, it has over 325 million users and offers more than 25,000 games in its catalog.

## Project Structure 

| Folder/File              | Description                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| **/data**                | Folder that stores datasets and files used by the API functions.                              |
| **/Feature_Notebooks**   | Folder containing Jupyter notebooks used for data transformation, analysis, and model development. |
| **/scripts**             | Folder containing scripts and utilities necessary for various tasks in the project.           |
| **Dockerfile**           | Configuration file for creating Docker containers, providing the necessary environment to run the application. |
| **requirements.txt**     | File listing dependencies and libraries required to run the project.                           |
| **gitignore**            | File specifying folders and files to be ignored by version control (git).                      |
| **gitattributes**        | File containing Git-specific attributes for certain files in the repository.                   |
| **LICENSE**              | MIT LICENSE - File specifying the terms under which the source code is shared.                 |
| **api_funct.py**         | Python file containing specific functions to be executed in the API.                            |
| **main.py**              | Main Python file serving as an entry point for the application, defining API configuration and execution. |
| **README.md**            | Main project documentation in English.                                                         |
| **README_ESP.md**        | Main project documentation in Spanish.                                                         |


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

## Functions and API Creation

Following the Transformation and Feature Engineering phase, the following functions have been developed based on the selected data and variables:

- **PlayTimeGenre:** Takes a genre as a parameter and returns the release year with the highest number of hours played for that genre.
- **UserForGenre:** Accepts a genre as input and provides information on the user with the highest playtime for the specified genre. It also returns a list of playtime hours per year for that user.
- **UsersRecommend:** Takes a year as input and produces a list of dictionaries. Each dictionary represents a game's position and its count of 'True' recommendations.
- **UsersNotRecommend:** Requires a year as input and outputs a list of dictionaries. Each dictionary signifies a game's position and its count of 'False' recommendations.
- **sentiment_analysis:** Given a year as input, returns a dictionary containing the count of reviews for each sentiment category in that year.

These functions are designed to be consumed through an API built with the Fast API framework.

## Recommendation Models

- Two recommendation models were developed: item-item and user-game.
- Memory-based algorithms were used, utilizing cosine similarity to measure similarities between games and users.
- Lists of 5 recommended games were generated for a specific game or user, respectively.

## Deployment

The API deployment in the cloud was executed using the Render platform, with automatic deployment triggered from GitHub. The deployment process involved the following steps:

- Creation of a Dockerfile for deployment, specifying the necessary versions and paths for containerization.
- Establishment of a new web service on render.com, connected to a current auxiliary repository (accessible [HERE](https://github.com/leocortes85/STEAM_API)), and utilizing Docker as the runtime environment.

*_(<span style="color: #dddddd;">Note: An auxiliary repository with reduced databases is employed for proper execution from Render, addressing its memory limitations.</span>)_*


This README provides an overview of the MLOps project for the Steam platform, highlighting key processes and outcomes. For detailed information on implementation, refer to the documentation and source code on the [GitHub repository](https://github.com/leocortes85/PI_MLOps_Steam). You can also access the API and explore the documentation at the [API link](https://mlops-steam-leo.onrender.com/).

To learn more about the creator of this project, visit his [LinkedIn profile](https://www.linkedin.com/in/leonardo-cort%C3%A9s-zambrano-13522295/) [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/leonardo-cort%C3%A9s-zambrano-13522295/)

