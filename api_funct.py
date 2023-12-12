# Importaciones
import pandas as pd
import operator
import warnings
warnings.filterwarnings("ignore")


#Load data

df_playtime_genre = pd.read_parquet('Data/parquet/playtime_genre.parquet')
df_user_for_genre = pd.read_parquet('Data/parquet/user_for_genre.parquet')
df_user_recommend = pd.read_parquet('Data/parquet/user_recommend.parquet')
df_sentiment_year = pd.read_parquet('Data/parquet/sentiment_year.parquet')


def Intro():
    '''
    Generates an HTML splash page for the Steam Video Game Query API.
    
    Returns:
    str: HTML code that displays the splash page.
    '''
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API Steam</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 20px;
                text-align: center;
            }

            h1 {
                color: #333;
                margin-bottom: 10px;
            }

            p {
                color: #666;
                font-size: 18px;
                margin-top: 10px;
            }

            a {
                color: #007bff;
                text-decoration: none;
            }

            a:hover {
                text-decoration: underline;
            }

            img {
                width: 50px;
                height: 20px;
                vertical-align: middle;
                margin-left: 5px;
            }

            .github-badge {
                display: inline-block;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <h1>Leonardo Cortes. IP1, 'Soy Henry' Data Bootcamp</h1>
        <h1>Steam Platform Video Game Query API</h1>
        <h1>Welcome!</h1>
        <p>To interact with available endpoints, explore the API documentation clicking the image.</p>
        <a href="/docs"><img src="https://img.asmedia.epimg.net/resizer/XsDeF1LjuA8ud6DsQpHUuq9Ropw=/644x362/cloudfront-eu-central-1.images.arcpublishing.com/diarioas/MWVSLOODJVBRDAIZ5DMRUDQIRM.jpg" alt="Steam Image" style="width: 500px; height: auto; margin-top: 20px;"></a>
    
        <p>For project details, check out the <a href="https://github.com/leocortes85/PI_MLOps_Steam" target="_blank" rel="noopener noreferrer" class="github-badge">GitHub repository <img alt="GitHub" src="https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github"></a></p>
        <p>More about Leonardo, visit his  <a href="https://www.linkedin.com/in/leonardo-cort%C3%A9s-zambrano-13522295/"> Linkedin profile <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin"></a></p>
    </body>
    </html>
        '''

def PlayTimeGenre(genre: str):
    """
    Returns the release year with the most hours played for the given genre.

    Parameters:
    - genre (str): Genre for which you want to obtain the release year with the most hours played.

    Returns:
    - dict: Dictionary with the release year with the most hours played for the specified genre.
    """
    # Convert the gender to lowercase to do the search regardless of upper or lower case
    genre_lower = genre.lower() if isinstance(genre, str) else None

    # Filter the DataFrame by the given gender
    genre_df = df_playtime_genre[df_playtime_genre['genres'].str.lower() == genre_lower]

    if genre_df.empty:
        return {f"No data avalible for genre {genre}": None}

    # Check for data before trying to get the index of the maximum value
    if not genre_df['playtime_forever'].empty:
        # Get the year with the most hours played
        max_playtime_year = genre_df.loc[genre_df['playtime_forever'].idxmax(), 'release_year']

        return {f"Release year with the most hours played for the genre {genre}": max_playtime_year}
    else:
        return {f"There is no data available for the gender {genre}": None}
    

    
def UserForGenre(genre: str):
    """
    Returns the user with the most hours played for the given genre and a list of hours played per year for that user.

    Parameters:
    - genre (str): Genre for which you want to obtain the user and the accumulation of hours played.

    Returns:
    - dict: Dictionary with the user with the most hours played and the list of hours played per year for that user.
    """
    
    # Convert the gender to lowercase to do the search regardless of upper or lower case
    genre_lower = genre.lower() if isinstance(genre, str) else None
    # Filter the DataFrame by the given gender
    genre_df = df_user_for_genre[df_user_for_genre['genres'].str.lower() == genre_lower]

    if genre_df.empty:
        return {"User with the most hours played for the genre": None, "Hours played per year": {}}

    # Group by user and add hours played
    user_playtime_sum = genre_df.groupby('user_id')['playtime_hours'].sum()

    # Take the user with the maximum sum of hours played
    max_playtime_user = user_playtime_sum.idxmax()

    # Filter the DataFrame by the specific user
    user_df = genre_df[genre_df['user_id'] == max_playtime_user]

    # Create a dictionary with the hours played per year for the mentioned user
    playtime_by_year = dict(zip(user_df['release_year'], user_df['playtime_hours']))

    return {f"User with the most hours played for the genre {genre}": max_playtime_user, "Hours played per year": playtime_by_year}


def UsersRecommend(year):
    '''
    This function takes a year as input and filters user reviews for that year, considering only recommended reviews.
    It then selects positive/neutral reviews (sentiment_analysis 1 or 2) and counts the recommendations for each game.
    The function returns the top 3 games with the highest recommendation counts in the specified year.

    Parameters:
    - year (int): The target year for filtering reviews.

    Returns:
    List of dictionaries, where each dictionary represents a top game and its recommendation count.
    Example:
    [{'Position 1: GameA': 30}, {'Position 2: GameB': 25}, {'Position 3: GameC': 20}]
    '''
    # Filter reviews for the given year and which are recommended
    filtered_reviews = df_user_recommend[(df_user_recommend['posted'] == year) & (df_user_recommend['recommend'] == True)]
    
    # Filter only positive/neutral reviews (sentiment_analysis 1 or 2)
    positive_reviews = filtered_reviews[filtered_reviews['sentiment_analysis'].isin([1, 2])]
    
    # Count recommendations per item
    recommendations_count = positive_reviews['item_name'].value_counts().reset_index()
    recommendations_count.columns = ['item_name', 'recommendations_count']
    
    # Get top 3
    top3_recommendations = recommendations_count.head(3)
    
    
    result = [{"Position {}: {}".format(i+1, row['item_name']): row['recommendations_count']} for i, row in top3_recommendations.iterrows()]
    
    return result

def UsersNotRecommend(year):
    '''
    This function takes a year as input and filters user reviews for that year, considering only recommended reviews.
    It then selects negative reviews (sentiment_analysis 0) and counts the recommendations for each game.
    The function returns the top 3 games with the lowest recommendation counts in the specified year.

    Parameters:
    - year (int): The target year for filtering reviews.

    Returns:
    List of dictionaries, where each dictionary represents a low top items and its recommendation count.
    Example:
    [{'Position 1: GameA': 30}, {'Position 2: GameB': 25}, {'Position 3: GameC': 20}]
    '''
    # Filter reviews for the given year that are not recommended
    filtered_reviews = df_user_recommend[(df_user_recommend['posted'] == year) & (df_user_recommend['recommend'] == False)]
    
    # Filter only negative reviews (sentiment_analysis 0)
    negative_reviews = filtered_reviews[filtered_reviews['sentiment_analysis'] == 0]
    
    # Count recommendations per item
    not_recommendations_count = negative_reviews['item_name'].value_counts().reset_index()
    not_recommendations_count.columns = ['item_name', 'not_recommendations_count']
    
    # Get low top 3
    top3_not_recommendations = not_recommendations_count.head(3)
    
    
    result = [{"Position {}: {}".format(i+1, row['item_name']): row['not_recommendations_count']} for i, row in top3_not_recommendations.iterrows()]
    
    return result


def sentiment_analysis(year):
    '''
    This function performs sentiment analysis on game reviews for a specified year. It filters reviews based on the release year
    and counts the number of reviews for each sentiment category (Negative, Neutral, Positive).

    Parameters:
    - year (int): The target year for filtering reviews.

    Returns:
    Dictionary containing the counts of reviews for each sentiment category.
    Example:
    {'Negative': 10, 'Neutral': 20, 'Positive': 30}
    '''

    # Filter reviews for the given year
    filtered_reviews = df_sentiment_year[df_sentiment_year['release_year'] == year]
   
    # Count the number of records for each sentiment analysis category
    sentiment_counts = filtered_reviews['sentiment_analysis'].value_counts().to_dict()
  
    # Create a dictionary with the categories and their quantities
    result = {
        'Negative': sentiment_counts.get(0, 0),
        'Neutral': sentiment_counts.get(1, 0),
        'Positive': sentiment_counts.get(2, 0)
    }
    
    return result
