import requests
import pandas as pd
import sqlalchemy
import sqlite3


header = {"Accept": "application/json", 
 "Content-Type": "application/json" ,
  "Authorization": "Bearer BQCaMXzoEQb4fHnSpaTV2XGVoKCY9bApmZ1xtnG0omf9ZMcJYiMleJNokQbLXgrn0RiZd8iQfRPvtAcsavRGrJNhLkZaqsu9QWb6V-1KenKiAZXz_opM8KrE5Sg0zXH13VRSe6WJbr6shSmLtYNyPTar3D8KfDXT40MN"

}
r = requests.get("https://api.spotify.com/v1/me/player/recently-played?limit=50",headers=header)


data = r.json()





print(data)

artist_name =[]
song_name =[]
popularity = []
played_time = []

for song in data['items']:
    song_name.append(song['track']['name'])
    popularity.append(song['track'] ['popularity'])
    artist_name.append(song['track']['album']['artists'][0]['name'])
    played_time.append(song['played_at'])

song_data = {
    'artist_name': artist_name,
    'song_name ' : song_name, 
    'popularity' : popularity,
    'played_time' : played_time
}

print()

print(song_data)
df = pd.DataFrame.from_dict(song_data,orient ='columns')

print(df)

    
# Loading the data
engine = sqlalchemy.create_engine("sqlite:///my_played_tracks.sqlite")

conn = sqlite3.connect('my_played_tracks.sqlite')
cursor = conn.cursor()

sql_query = """
    CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        timestamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
    )
    """

cursor.execute(sql_query)
print("Opened database successfully")

try:
    song_df.to_sql("my_played_tracks", engine, index=False, if_exists='append')
except:
    print("Data already exists in the database")

conn.close()
print("Close database successfully")
    






