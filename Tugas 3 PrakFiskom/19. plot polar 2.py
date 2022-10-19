import numpy as np
import matplotlib.pyplot as plt
N = 8
theta = np.arange(0.,2 * np.pi, 2 * np.pi / N)
radius = np.array([4,7,5,3,1,5,6,7])
plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
colors = np.array(['lightgreen', 'darkred', 'navy', 'brown', 'violet', 'plum', 'purple', 'yellow', 'green'])
bars = plt.bar(theta, radius, width=(2*np.pi/N), bottom=0.0, color=colors)
plt.show()
