"""import pandas as pd
df=pd.read_csv("school.csv")

df["average_student"]=df[["math","physics","cs"]].mean(axis=1).round(2)
classaveragePerSubject=df[["math","physics","cs"]].mean(axis=0).round(2)
CPS=pd.Series(classaveragePerSubject,index=["math","physics","cs"])
df=df.sort_values(by="average_student",ascending=False)
lastpoint=df.iloc[-1]["average_student"]
firstStudent=df.iloc[0]
classaverage=df["average_student"].mean(axis=0).__round__(2)
result=df[["math","physics","cs"]].agg(["max","min","mean"])
print(result)

print(df)
print(CPS) 
print("The last point is:",lastpoint)
print("The first student is:\n",firstStudent)
print("The class average is:",classaverage)"""
import pandas as pd
df=pd.read_csv("games.csv")
agg=df[["rating","hour_played"]].agg(["max","min"])
avg_hour=df["hour_played"].mean(axis=0).__round__(2)
most_played=df.sort_values(by="hour_played",ascending=False).iloc[:11,:]
print(most_played)
print("The average hour played is:",avg_hour)
print(agg)


