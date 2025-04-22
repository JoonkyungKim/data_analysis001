from analysis import load_data, preprocess_data, get_summary_stats
from visualization import plot_content_by_year, plot_top_genres, plot_top_actors


df = load_data("data/netflix_titles.csv")
df = preprocess_data(df)


get_summary_stats(df)


plot_content_by_year(df, save_path="outputs/content_by_year.png")
plot_top_genres(df, save_path="outputs/top_genres.png")
plot_top_actors(df, save_path="outputs/top_actors.png")
