import matplotlib.pyplot as plt

def plot_genre(df):
    genre = df.groupby("Genre")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum()
    genre_pct = genre.div(genre.sum(axis=1), axis=0)    #row wise %

    plt.figure(figsize=(12, 6))
    genre_pct.plot(kind="bar", stacked=True)
    plt.title("Genre Sales by Region")
    plt.ylabel("% of Total Sales")
    plt.xlabel("Genre")
    plt.tight_layout()
    plt.savefig("genre_regional_sales.png")
    plt.close()

                        # could refactor this and plot_genre into one reusable function later
                        # but left it separate for clarity

def plot_platform(df):
    platform = df.groupby("Platform")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum()
    platform_pct = platform.div(platform.sum(axis=1), axis=0)


    plt.figure(figsize=(14, 6))
    platform_pct.plot(kind="bar", stacked=True)
    plt.title("Platform Sales by Region")
    plt.ylabel("% of Total Sales")
    plt.xlabel("Platform")
    plt.tight_layout()
    plt.savefig("platform_chart_region.png")
    plt.close()
