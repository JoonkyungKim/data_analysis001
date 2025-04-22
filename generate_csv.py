import pandas as pd
import os

os.makedirs("data", exist_ok=True)


# Sample data
data = {
    'show_id': ['s1', 's2', 's3', 's4', 's5'],
    'type': ['Movie', 'TV Show', 'Movie', 'Movie', 'TV Show'],
    'title': ['Inception', 'Stranger Things', 'The Irishman', 'Extraction', 'The Crown'],
    'director': ['Christopher Nolan', 'Duffer Brothers', 'Martin Scorsese', 'Sam Hargrave', 'Peter Morgan'],
    'cast': ['Leonardo DiCaprio, Tom Hardy', 'Millie Bobby Brown, David Harbour',
             'Robert De Niro, Al Pacino', 'Chris Hemsworth', 'Olivia Colman, Tobias Menzies'],
    'country': ['United States', 'United States', 'United States', 'India', 'United Kingdom'],
    'date_added': ['January 1, 2020', 'March 15, 2021', 'November 27, 2019', 'July 10, 2020', 'June 5, 2021'],
    'release_year': [2010, 2016, 2019, 2020, 2016],
    'rating': ['PG-13', 'TV-14', 'R', 'R', 'TV-MA'],
    'duration': ['148 min', '3 Seasons', '209 min', '117 min', '4 Seasons'],
    'listed_in': ['Action, Sci-Fi', 'Sci-Fi, Thriller', 'Crime, Drama', 'Action, Thriller', 'Drama, History'],
    'description': [
        'A thief who steals corporate secrets through dream-sharing technology.',
        'A group of young friends witness supernatural forces and secret experiments.',
        'An aging hitman recalls his past with the mob.',
        'A black ops mercenary’s mission turns into a fight for survival.',
        'The political rivalries of Queen Elizabeth II’s reign.'
    ]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/netflix_titles.csv", index=False)
print("✅ netflix_titles.csv has been created in the 'data' folder.")
