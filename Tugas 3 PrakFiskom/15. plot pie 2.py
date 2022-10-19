import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'lain lain', 'samsung', 'apple', 'huawei','oppo','vivo'
sizes = [42, 21, 14, 9, 8, 7]
explode = (0, 1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
colors = 'red', 'green', 'pink', 'blue', 'black', 'orange'
plt.title('diagram pie market share samsung')
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
