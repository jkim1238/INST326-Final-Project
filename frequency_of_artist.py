import matplotlib.pyplot as plt
import csv
import collections

top_artists = collections.Counter()

# loading csv file into csvreader:
# artists is in column 1 (row[1])
with open('hot_100_12_nov.csv') as input_file:
    for row in csv.reader(input_file, delimiter=','):
        top_artists[row[1]] += 1

# get top 10
top_artists = top_artists.most_common(10)
names, values = zip(*top_artists)

fig, ax = plt.subplots()

plt.bar(names, values, color='lightseagreen')
plt.title("Top 10 Artists")
plt.ylabel("Count")
plt.xticks(rotation=90)
for i, (tag, count) in enumerate(top_artists):
    plt.text(i, count, f' {count} ',
             ha='center', va='bottom', color='black')
plt.xlim(-0.6, len(names)-0.4) # optionally set tighter x lims
plt.tight_layout() # change the whitespace such that all labels fit nicely
plt.show()