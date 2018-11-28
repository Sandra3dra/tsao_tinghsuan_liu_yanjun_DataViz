import csv
import matplotlib.pyplot as plt
import numpy as np

categories = []
japan = []

with open('data/OlympicsWinter.csv', encoding="utf-8") as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "JPN":
			japan.append([int(row[0]), row[5], row[6], row[7]])
			line_count += 1

print("Total medals for Japan:", len(japan))

print("processed", line_count, "rows of data")


japan_gold = []
japan_silver = []
japan_bronze = []

categories = []

for medal in japan:
	if medal[3] == "Gold":
		japan_gold.append(medal)

	if medal[3] == "Silver":
		japan_silver.append(medal)

	if medal[3] == "Bronze":
		japan_bronze.append(medal)


print(len(japan_gold), "Gold medals were won by Japan from 1924 to 2014")
print(len(japan_silver), "Silver medals were won by Japan from 1924 to 2014")
print(len(japan_bronze), "Bronze medals were won by Japan from 1924 to 2014")

totalMedals = len(japan_gold) + len(japan_silver) + len(japan_bronze)

#percentage of all medals
gold_percentage = int(len(japan_gold) / totalMedals * 100)
silver_percentage = int(len(japan_silver) / totalMedals * 100)
bronze_percentage = int(len(japan_bronze) / totalMedals * 100)

# print(gold_percentage, silver_percentage, bronze_percentage)

print("processed", line_count, "lines of data. Total medals:", totalMedals)

#do the pie chart / visualization
#now we can plot stuff!
labels = "Gold", "Silver", "Bronze"
sizes = [gold_percentage, silver_percentage, bronze_percentage]
colors = ["gold", "silver", "firebrick"]
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medal Wins - Historic Medal Counts of Japan")
plt.xlabel("Medal Counts Since 1924")
plt.show()


gold_1924 = []
gold_1928 = []
gold_1932 = []
gold_1936 = []
gold_1940 = []
gold_1944 = []
gold_1948 = []
gold_1952 = []
gold_1956 = []
gold_1960 = []
gold_1964 = []
gold_1968 = []
gold_1972 = []
gold_1976 = []
gold_1980 = []
gold_1984 = []
gold_1988 = []
gold_1992 = []
gold_1994 = []
gold_1998 = []
gold_2002 = []
gold_2006 = []
gold_2010 = []
gold_2014 = []


for medal in japan:
	if medal[0] == 1924 and medal[3] == "Gold":
		gold_1924.append(medal)

	if medal[0] == 1928 and medal[3] == "Gold":
		gold_1928.append(medal)

	if medal[0] == 1932 and medal[3] == "Gold":
		gold_1932.append(medal)

	if medal[0] == 1936 and medal[3] == "Gold":
		gold_1936.append(medal)

	if medal[0] == 1940 and medal[3] == "Gold":
		gold_1940.append(medal)

	if medal[0] == 1944 and medal[3] == "Gold":
		gold_1944.append(medal)

	if medal[0] == 1948 and medal[3] == "Gold":
		gold_1948.append(medal)

	if medal[0] == 1952 and medal[3] == "Gold":
		gold_1952.append(medal)

	if medal[0] == 1956 and medal[3] == "Gold":
		gold_1956.append(medal)

	if medal[0] == 1960 and medal[3] == "Gold":
		gold_1960.append(medal)

	if medal[0] == 1964 and medal[3] == "Gold":
		gold_1964.append(medal)

	if medal[0] == 1968 and medal[3] == "Gold":
		gold_1968.append(medal)

	if medal[0] == 1972 and medal[3] == "Gold":
		gold_1972.append(medal)

	if medal[0] == 1976 and medal[3] == "Gold":
		gold_1976.append(medal)

	if medal[0] == 1980 and medal[3] == "Gold":
		gold_1980.append(medal)

	if medal[0] == 1984 and medal[3] == "Gold":
		gold_1984.append(medal)

	if medal[0] == 1988 and medal[3] == "Gold":
		gold_1988.append(medal)

	if medal[0] == 1992 and medal[3] == "Gold":
		gold_1992.append(medal)

	if medal[0] == 1994 and medal[3] == "Gold":
		gold_1994.append(medal)

	if medal[0] == 1998 and medal[3] == "Gold":
		gold_1998.append(medal)

	if medal[0] == 2002 and medal[3] == "Gold":
		gold_2002.append(medal)

	if medal[0] == 2006 and medal[3] == "Gold":
		gold_2006.append(medal)

	if medal[0] == 2010 and medal[3] == "Gold":
		gold_2010.append(medal)

	if medal[0] == 2014 and medal[3] == "Gold":
		gold_2014.append(medal)

print("Japan won", len(gold_1924), "gold medals in 1924")
print("Japan won", len(gold_1928), "gold medals in 1928")
print("Japan won", len(gold_1932), "gold medals in 1932")
print("Japan won", len(gold_1936), "gold medals in 1936")
print("Japan won", len(gold_1940), "gold medals in 1940")
print("Japan won", len(gold_1944), "gold medals in 1944")
print("Japan won", len(gold_1948), "gold medals in 1948")
print("Japan won", len(gold_1952), "gold medals in 1952")
print("Japan won", len(gold_1956), "gold medals in 1956")
print("Japan won", len(gold_1960), "gold medals in 1960")
print("Japan won", len(gold_1964), "gold medals in 1964")
print("Japan won", len(gold_1968), "gold medals in 1968")
print("Japan won", len(gold_1972), "gold medals in 1972")
print("Japan won", len(gold_1976), "gold medals in 1976")
print("Japan won", len(gold_1980), "gold medals in 1980")
print("Japan won", len(gold_1984), "gold medals in 1984")
print("Japan won", len(gold_1988), "gold medals in 1988")
print("Japan won", len(gold_1992), "gold medals in 1992")
print("Japan won", len(gold_1994), "gold medals in 1994")
print("Japan won", len(gold_1998), "gold medals in 1998")
print("Japan won", len(gold_2002), "gold medals in 2002")
print("Japan won", len(gold_2006), "gold medals in 2006")
print("Japan won", len(gold_2010), "gold medals in 2010")
print("Japan won", len(gold_2014), "gold medals in 2014")

print("processed", line_count, "rows of data")

# I tried to create a line chart but failed... and i dont want to delete my hard work(although it is basically trash)
# gold_1924 = len(gold_1924)
# gold_1928 = len(gold_1928)
# gold_1932 = len(gold_1932)
# gold_1936 = len(gold_1936)
# gold_1940 = len(gold_1940)
# gold_1944 = len(gold_1944)
# gold_1948 = len(gold_1948)
# gold_1952 = len(gold_1952)
# gold_1956 = len(gold_1956)
# gold_1960 = len(gold_1960)
# gold_1964 = len(gold_1964)
# gold_1968 = len(gold_1968)
# gold_1972 = len(gold_1972)
# gold_1976 = len(gold_1976)
# gold_1980 = len(gold_1980)
# gold_1984 = len(gold_1984)
# gold_1988 = len(gold_1988)
# gold_1992 = len(gold_1992)
# gold_1994 = len(gold_1994)
# gold_1998 = len(gold_1998)
# gold_2002 = len(gold_2002)
# gold_2006 = len(gold_2006)
# gold_2010 = len(gold_2010)
# gold_2014 = len(gold_2014)

# year = "1924", "1928", "1932", "1936", "1940", "1944", "1948", "1952", "1956", "1960", "1964", "1968", "1972", "1976", "1980", "1984", "1988", "1992", "1996", "2002", "2006", "2010", "2014"
# medalsbyyear = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 3.0, 3.0, 8.0, 0.0, 1.0, 0.0, 1.0]

# plt.plot(year, medalsbyyear, color='r')
# plt.xlabel('Gold Medals Won From 1924 to 2014')
# plt.ylabel('Numbers Of Gold Medals')
# plt.title('Gold Medals Won By Japan')
# plt.show()

# chart two
year = ("2002", "2006", "2010", "2014")
sizes = [0, 1, 0, 1]
index = np.arange(len(year))
# colors = ["r"]align='center', 

plt.bar(index, sizes, color="r")
plt.ylabel('Numbers Of Gold Medals')
plt.xticks(index, year)
# plt.axis([0, len(sizes), -1, max(sizes)])
plt.title("Gold Medals Won By Japan After The Year Of 2000")
plt.show()

