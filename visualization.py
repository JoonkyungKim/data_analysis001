import matplotlib.pyplot as plt

def plot_content_by_year(df, save_path=None):
    df_year = df.groupby(['year_added', 'type']).size().unstack(fill_value=0)
    df_year.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title("Content Added by Year")
    plt.ylabel("Count")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.close()

def plot_top_genres(df, save_path=None):
    top_genres = df['listed_in'].value_counts().head(5)
    top_genres.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6))
    plt.title("Top Genres")
    plt.ylabel("")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.close()

def plot_top_actors(df, save_path=None):
    actors = df['cast'].dropna().str.split(', ').explode()
    top_actors = actors.value_counts().head(5)
    top_actors.plot(kind='barh', figsize=(8, 5))
    plt.title("Top 5 Actors")
    plt.xlabel("Appearances")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.close()
