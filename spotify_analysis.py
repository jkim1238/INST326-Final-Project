import argparse
import sys
import csv
import collections
import matplotlib.pyplot as plt
import pandas
import spotipy


def get_spotify_data():
    from spotipy.oauth2 import SpotifyClientCredentials

    sp = spotipy.Spotify(auth_manager=
    SpotifyClientCredentials(
        client_id="8f435079637248efa9508bb5b03900af",
        client_secret="525b9a3209c04587ae12543e5c17bbf4"))

    sp.trace = False

    playlist = sp.playlist("6UeSakyzhiEt4NB3UAd6NQ?si=1Rwmvg38SYy4Tg2RAaGEKQ")

    # Create empty dataframe
    playlist_features_list = ["artist", "album", "track_name", "track_id",
                              "danceability", "energy", "key", "loudness",
                              "mode", "speechiness", "instrumentalness",
                              "liveness", "valence", "tempo", "duration_ms",
                              "time_signature"]

    playlist_df = pandas.DataFrame(columns=playlist_features_list)

    # Loop through every track in the playlist, extract features and append the
    # features to the playlist df
    for track in playlist["tracks"]["items"]:

        # Create dictionary and get metadata
        playlist_features = {
            "artist": track["track"]["album"]["artists"][0]["name"],
            "album": track["track"]["album"]["name"],
            "track_name": track["track"]["name"],
            "track_id": track["track"]["id"]
        }

        # Get audio features
        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]

        # Concat the dfs
        track_df = pandas.DataFrame(playlist_features, index=[0])
        playlist_df = pandas.concat([playlist_df, track_df], ignore_index=True)

    return playlist_df


class Plot:

    def __init__(self, path=None):
        if path is None:
            self.data_frame = get_spotify_data()
        else:
            self.path = pandas.read_csv(path)

    def bar_plot(self):
        top_artists = collections.Counter()

        # loading csv file into csvreader:
        # artists is in column 1 (row[1])
        with open(self.path) as input_file:
            for row in csv.reader(input_file, delimiter=','):
                top_artists[row[1]] += 1

        # get top 10
        top_artists = top_artists.most_common(10)
        names, values = zip(*top_artists)

        fig, ax = plt.subplots()

        plt.bar(names, values, color='lightseagreen')
        plt.title("Top 10 Artist Occurrences")
        plt.ylabel("Count")
        plt.xticks(rotation=90)
        for i, (tag, count) in enumerate(top_artists):
            plt.text(i, count, f' {count} ',
                     ha='center', va='bottom', color='black')
        # optionally set tighter x lims
        plt.xlim(-0.6, len(names) - 0.4)
        # change the whitespace such that all labels fit nicely
        plt.tight_layout()
        plt.show()

    def bar_plot_top_10_occurrences(self):
        # Get top 10 occurrences.
        axes = self.data_frame["artist"].value_counts().nlargest(10).plot.bar(
            rot=0,
            color="turquoise",
            title="Top 10 Artist Occurrences"
        )

        # Set labels.
        axes.set_xlabel("Artist", fontsize=12)
        axes.set_ylabel("Occurrences", fontsize=12)

        # Add values above bars.
        for p in axes.patches:
            axes.annotate("%.0f" % p.get_height(),
                          (p.get_x() + p.get_width() / 2., p.get_height()),
                          ha='center', va='center', xytext=(0, 10),
                          textcoords='offset points')

        # Show plot.
        plt.show()

    def save_to_csv_file(self):
        self.data_frame.to_csv('hot_100.csv')


def main(path):
    # Create an instance of Plot.
    plot = Plot(path)

    # Show menu.
    print(39 * '-')
    print("MENU")
    print(39 * '-')
    print("1. Bar Plot - Top 10 Artist Occurrences")
    print("2. Save to CSV file")
    print("3. Exit")
    print(39 * '-')

    while True:
        # Get choice.
        choice = int(input("Enter choice: "))

        # Handle choice.
        if choice == 1:
            plot.bar_plot_top_10_occurrences()
        elif choice == 2:
            plot.save_to_csv_file()
            print("Saved to CSV file...")
            break
        elif choice == 3:
            print("Exiting...")
            break
        else:
            input("Error. Press ENTER to continue...")


def parse_args(my_args_list):
    """Parses the command line arguments for the program;
    this will result in a namespace object, which you should return.

    Args:
        my_args_list (str): a list of strings containing the command line
            arguments for the program.

    Returns:
        namespace object: the command line arguments namespace object.
    """

    # Create a new Parser instance.
    parser = argparse.ArgumentParser("Analyze a dataset from Spotify's "
                                     "Billboard Hot 100.")

    # Optional arguments.
    # The path to the text file.
    parser.add_argument("-p", "--path",
                        type=str,
                        help="the path to the csv file")

    # Parsing the list using the arguments defined in the parser object.
    # Use the parse_args() method of your ArgumentParser instance to parse the
    # list of strings that was passed to your function; this will result in a
    # namespace object, which you should return.
    args = parser.parse_args(my_args_list)

    # Return the namespace object.
    return args


if __name__ == '__main__':
    # Pass sys.argv[1:] to parse_args() and store the result in a
    # variable.
    args = parse_args(sys.argv[1:])

    # Call the main() function.
    main(args.path)
