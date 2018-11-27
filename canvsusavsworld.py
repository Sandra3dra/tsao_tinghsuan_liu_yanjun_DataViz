import csv
import matplotlib.pyplot as plt
import numpy as np

categories = []
canada = []
america = []
world = []

with open('data/OlympicsWinter.csv', encoding="utf-8") as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "CAN":
			canada.append([int(row[0]), row[5], row[6], row[7]])
		elif row[4] == "USA":
			america.append([int(row[0]), row[5], row[6], row[7]])
		else:
			world.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1

print("Total medals for Canada:", len(canada))
print("Total medals for America:", len(america))
print("Total medals for everyone else:", len(world))

print("processed", line_count, "rows of data")

totalMedals = len(canada) + len(america) + len(world)
# gold_percentage = int(len(golds) / totalMedals * 100)
canada_percentage = int(len(canada) / totalMedals * 100)
america_percentage = int(len(america) / totalMedals * 100)
world_percentage = int(len(world) / totalMedals * 100)

# chart one
labels = "Canada", "America", "Everyone Else"
sizes = [canada_percentage, america_percentage, world_percentage]
colors = ["orangered", "navy", "orchid"]
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medal Wins - Historic Medal Counts")
plt.xlabel("Medal Counts From 1924 to 2014")
plt.show()


# chart two
labels = "Canada", "America", "Everyone Else"
sizes = [len(canada), len(america), len(world)]
index = np.arange(len(labels))
colors = ["orangered", "navy", "orchid"]

plt.bar(index, sizes, align='center', color=colors)
plt.ylabel('Numbers of Medals')
plt.xticks(index, labels)
plt.title("Medals won From 1924 To 2014")
plt.show()
