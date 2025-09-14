import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

IPL_BLUE = "#1C3AA9"
IPL_YELLOW = "#FFD700"
IPL_ORANGE = "#FF7300"
IPL_WHITE = "#FFFFFF"

df = pd.read_csv(r"C:\Users\USER\OneDrive\New folder\New folder\netflx\ipl_2025_auction_players.csv")
df["Sold"] = pd.to_numeric(df["Sold"], errors="coerce")

team_spending = df.groupby("Team")["Sold"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6), facecolor=IPL_BLUE)
bars = plt.bar(team_spending.index, team_spending.values, color=IPL_YELLOW, edgecolor=IPL_WHITE)
plt.title("Team-wise Spending (in Crores)", fontsize=18, color=IPL_WHITE, pad=15)
plt.xlabel("Teams", color=IPL_WHITE, fontsize=12)
plt.ylabel("Total Spending", color=IPL_WHITE, fontsize=12)
plt.xticks(rotation=45, color=IPL_WHITE)
plt.yticks(color=IPL_WHITE)

for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f"{bar.get_height():.1f}", 
             ha='center', va='bottom', color=IPL_WHITE, fontsize=9)

try:
    logo = mpimg.imread(r"C:\Users\USER\OneDrive\New folder\New folder\netflx\412454.png")
    plt.figimage(logo, xo=700, yo=250, alpha=0.6, zorder=-1)
except:
    pass

plt.tight_layout()
plt.show()

type_distribution = df.groupby("Type")["Players"].count()

plt.figure(figsize=(7, 7), facecolor=IPL_BLUE)
plt.pie(type_distribution.values, labels=type_distribution.index, autopct='%1.1f%%',
        startangle=140, colors=[IPL_YELLOW, IPL_ORANGE, IPL_WHITE], textprops={'color': IPL_BLUE})
plt.title("Player Type Distribution", fontsize=18, color=IPL_WHITE, pad=15)

try:
    logo = mpimg.imread(r"C:\Users\USER\OneDrive\New folder\New folder\netflx\ipl_logo.png")
    plt.figimage(logo, xo=250, yo=200, alpha=0.6, zorder=-1)
except:
    pass

plt.tight_layout()
plt.show()

top_players = df.sort_values("Sold", ascending=False).head(10)

plt.figure(figsize=(10, 6), facecolor=IPL_BLUE)
bars = plt.barh(top_players["Players"], top_players["Sold"], color=IPL_ORANGE, edgecolor=IPL_WHITE)
plt.title("Top 10 Most Expensive Players", fontsize=18, color=IPL_WHITE, pad=15)
plt.xlabel("Sold Price (in Crores)", color=IPL_WHITE, fontsize=12)
plt.ylabel("Players", color=IPL_WHITE, fontsize=12)
plt.xticks(color=IPL_WHITE)
plt.yticks(color=IPL_WHITE)
plt.gca().invert_yaxis()

for bar in bars:
    plt.text(bar.get_width()+0.3, bar.get_y()+bar.get_height()/2, f"{bar.get_width():.1f}", 
             ha='left', va='center', color=IPL_WHITE, fontsize=9)

try:
    logo = mpimg.imread(r"C:\Users\USER\OneDrive\New folder\New folder\netflx\ipl_logo.png")
    plt.figimage(logo, xo=650, yo=150, alpha=0.6, zorder=-1)
except:
    pass

plt.tight_layout()
plt.show()
