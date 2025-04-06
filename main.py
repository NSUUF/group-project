from load_data import get_data
from platform_genre_charts import plot_genre, plot_platform


df = get_data()     #get cleaned dataset


plot_genre(df)      #generate both charts
plot_platform(df)

print("charts saved")
