import csv
import matplotlib.pyplot as plt
import numpy as np

categories = []
male = []
female = []

with open('data/OlympicsWinter.csv', encoding="utf-8") as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[5] == "Men":
			male.append([int(row[0]), row[5], row[6], row[7]])
			line_count += 1
		elif row[5] == "Women":
			female.append([int(row[0]), row[5], row[6], row[7]])

print("Total medals for Men:", len(male))
print("Total medals for Women:", len(female))

print("processed", line_count, "rows of data")

totalMedals = len(male) + len(female)

male_percentage = int(len(male) / totalMedals * 100)
female_percentage = int(len(female) / totalMedals * 100)

# chart one
labels = "Male", "Female"
sizes = [male_percentage, female_percentage]
colors = ["r", "b"]
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medal Wins - Male VS Female")
plt.xlabel("Medal Counts From 1924 to 2014")
plt.show()

male_2002 = []
male_2006 = []
male_2010 = []
male_2014 = []

for number in male:
	if number[0] == 2002 and number[1] == "Men":
		male_2002.append(number)

	if number[0] == 2006 and number[1] == "Men":
		male_2006.append(number)

	if number[0] == 2010 and number[1] == "Men":
		male_2010.append(number)

	if number[0] == 2014 and number[1] == "Men":
		male_2014.append(number)	

print(len(male_2002), "men won medals in 2002")
print(len(male_2006), "men won medals in 2006")
print(len(male_2010), "men won medals in 2010")
print(len(male_2014), "men won medals in 2014")

print("processed", line_count, "rows of data")

female_2002 = []
female_2006 = []
female_2010 = []
female_2014 = []

for number in female:
	if number[0] == 2002 and number[1] == "Women":
		female_2002.append(number)

	if number[0] == 2006 and number[1] == "Women":
		female_2006.append(number)

	if number[0] == 2010 and number[1] == "Women":
		female_2010.append(number)

	if number[0] == 2014 and number[1] == "Women":
		female_2014.append(number)	

print(len(female_2002), "women won medals in 2002")
print(len(female_2006), "women won medals in 2006")
print(len(female_2010), "women won medals in 2010")
print(len(female_2014), "women won medals in 2014")

print("processed", line_count, "rows of data")


# data to plot
maletotal = (len(male_2002), len(male_2006), len(male_2010), len(male_2014))
femaletotal = (len(female_2002), len(female_2006), len(female_2010), len(female_2014))
 
# create plot
fig, ax = plt.subplots()
n_groups = 4
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, maletotal, bar_width, alpha=opacity, color='b', label='Male')
 
rects2 = plt.bar(index + bar_width, femaletotal, bar_width, alpha=opacity, color='r', label='Female')
 
plt.xlabel('Years')
plt.ylabel('Numbers')
plt.title('Numbers of Male and Female Won Medals Since 2002')
plt.xticks(index + bar_width, ("2002", "2006", "2010", "2014"))
plt.legend()
 
plt.tight_layout()
plt.show()
