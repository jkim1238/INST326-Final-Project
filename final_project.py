
# Import Spotify API/module/package/library -> functions/methods/classes you can
# use.
import spotipy
import pandas

from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=
                     SpotifyClientCredentials(
                         client_id="8f435079637248efa9508bb5b03900af",
                         client_secret="525b9a3209c04587ae12543e5c17bbf4"))

sp.trace = False

# Get Billboard Top 100 playlist
playlist = sp.playlist("6UeSakyzhiEt4NB3UAd6NQ?si=1Rwmvg38SYy4Tg2RAaGEKQ")

# Create empty dataframe
playlist_features_list = ["artist", "album", "track_name", "track_id",
                          "danceability", "energy", "key", "loudness", "mode",
                          "speechiness", "instrumentalness", "liveness",
                          "valence", "tempo", "duration_ms", "time_signature"]

playlist_df = pandas.DataFrame(columns=playlist_features_list)

# Loop through every track in the playlist, extract features and append the features to the playlist df
for track in playlist["tracks"]["items"]:
  
    # Create empty dict
    playlist_features = {}
    
    # Get metadata
    playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
    playlist_features["album"] = track["track"]["album"]["name"]
    playlist_features["track_name"] = track["track"]["name"]
    playlist_features["track_id"] = track["track"]["id"]

    # Get audio features
    audio_features = sp.audio_features(playlist_features["track_id"])[0]
    for feature in playlist_features_list[4:]:
        playlist_features[feature] = audio_features[feature]

    # Concat the dfs
    track_df = pandas.DataFrame(playlist_features, index=[0])
    playlist_df = pandas.concat([playlist_df, track_df], ignore_index=True)

# Convert to csv file
playlist_df.to_csv('hot100.csv')
