import pandas as pd
import matplotlib.pyplot as plt

read1 = pd.read_csv("games.csv").sort_values(by="hour_played", ascending=False).head(15)
#read2=read1.groupby(["genres"]).agg({"hour_played":"sum","rating":"mean"}).sort_values(by="hour_played",ascending=False).head(15).reset_index()
"""plt.scatter(x=read1["hour_played"], y=read1["rating"])
for ind, va in read1[["hour_played", "rating", "name"]].iterrows():
    plt.text(va["hour_played"], va["rating"], va["name"], fontsize=8, ha='center',va ='bottom')
plt.show()"""
"""print(read2)
plt.pie(read2["hour_played"], labels=read2["genres"], startangle=140,labeldistance=1.1,autopct='%1.1f%%')
plt.legend(labels=read2["genres"], loc="lower left", bbox_to_anchor=(-0.29, -0.1), fontsize='small')

plt.title("Top 15 Genres by Total Hours Played")
plt.show()"""
plt.hist(read1["hour_played"], bins=5, color="orange", edgecolor="black")
plt.xlabel("Hours Played")
plt.ylabel("Count")
plt.title("Histogram of Hours Played")
print(read1["hour_played"].describe())
plt.show()


# فلترة على الألعاب اللي فيها Action و RPG فقط
read1_filtered = read1[read1["genres"] == "['Action', 'RPG']"].sort_values(by="hour_played", ascending=False)

"""pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
axis_ax=read2.plot(x="genres",y="hour_played",color="b",kind="bar")
axis_ay=read2.plot(x="genres",y="rating",color="r",marker='o',secondary_y=True,ax=axis_ax)
for ind,vl in enumerate(read2["hour_played"]):
    axis_ax.text(ind,vl,str(vl),ha="center",va="bottom")
for ind,vl in enumerate(read2["rating"]):
    axis_ay.text(ind,vl,str(round(vl,2)),ha="center",va="top")    
axis_ax.set_xticklabels(axis_ax.get_xticklabels(),rotation=45)"""
#read1_filtered.plot(x="hour_played", y="rating",kind="bar", title="Action RPG Games: Hours Played vs Rating", figsize=(10, 6))
#plt.show()

# دابا نقدر نطبع الأعمدة اللي بغينا
#print(read1_filtered[["genres","rating","hour_played","name"]].sort_values(by="hour_played",ascending=False).head(15))
#df=read1.groupby(["genres", "name"]).agg({"name":"count","rating":"mean","hour_played":"sum"}).sort_values(by="hour_played",ascending=False)
#df.to_csv("games_grouped.csv")


"""listGta["released"]=pd.to_datetime(listGta["released"],errors="coerce")
listGta["year"]=listGta["released"].dt.year
listGta=listGta.sort_values(by="year",ascending=True)
print(listGta[["name","year","rating"]].describe())
x=listGta["year"]
y=listGta["rating"]
plt.plot(x,y,marker="o")
plt.title("GTA Rating Over Years")
plt.xlabel("Release Year")
plt.ylabel("Rating")
plt.xticks(rotation=45)"""




