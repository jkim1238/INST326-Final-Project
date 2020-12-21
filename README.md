# Spotify Billboard Hot 100 Analysis [![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

<p align="center">
  <img src="https://imgur.com/6Mexw7E.png" />
</p>

A program that will analyze a dataset from Spotify’s Billboard Hot 100.

Our project will be able to identify popular genres, artists, and audio metrics that makes a song reach The Hot 100. The project will be able to extract from the selected dataset and visualize it with graphs such as pie charts and bar graphs using spotipy and matplotlib modules in Python. Our project will not be creating our own plotting modules or analyzing songs outside The Hot 100.

![Imgur](https://imgur.com/zl25v2f.png)

## Summary

  - [Scope](#scope)
  - [Project Breakdown and Division of Labor](#project-breakdown-and-division-of-labor)
  - [Meetings and Communication](#meetings-and-communication)
  - [Schedule and Milestones](#schedule-and-milestones)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Bibliography](#bibliography)
  - [Authors](#authors)

## Scope

Our project will be able to identify popular genres, artists, and audio metrics that makes a song reach The Hot 100. The project will be able to extract from the selected dataset and visualize it with graphs such as pie charts and bar graphs using spotipy and matplotlib modules in Python. Our project will not be creating our own plotting modules or analyzing songs outside The Hot 100.

## Project Breakdown and Division of Labor

The main software components will be scripts that will retrieve the data with spotipy and read data from the .csv file which will plot a graph based on a specific metric (ex. frequency of genre, frequency of artist, frequency of album).

The non-programming task is learning spotipy API and matplotlib modules which will be handled by the researcher.

## Meetings and Communication

Every Saturday evening on Discord or Zoom video call.

## Schedule and Milestones

  - Research spotipy API and matplotlib module
  - Retrieve dataset
  - Program a graph each week
  
## Installation

Besides needing the latest version of Python installed, you will also need to install the matplotlib, spotipy, and pandas Python library. This can be accomplished by running the following code in the terminal you are using:

```
pip install matplotlib
pip install spotipy
pip install pandas
```

## Usage

usage: Analyze a dataset from Spotify's Billboard Hot 100. [-h] [-p PATH]

optional arguments:  
  -h, --help            show this help message and exit  
  -p PATH, --path PATH  the path to the csv file

```
python spotify_analysis.py
```
or
```
python spotify_analysis.py [-p PATH]
```
or
```
python spotify_analysis.py [--path PATH]
```

**Click image for Youtube Presentation/Usage**

<p align="center">
  [INST326 Final Project Presentation Spotify Analysis](readme-files/INST326_Final_Project_Presentation_Spotify_Analysis.gif)(https://www.youtube.com/watch?v=ZD7cg94gz2U)
</p>

## Bibliography

  - https://www.billboard.com/charts/hot-100
  - https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/

## Authors

  - **Jiin Kim** - *Researcher* -
    [jkim1238](https://github.com/jkim1238)
  - **Nour Fouladi** - *Analyst* -
    [TODO](https://github.com/jkim1238)
