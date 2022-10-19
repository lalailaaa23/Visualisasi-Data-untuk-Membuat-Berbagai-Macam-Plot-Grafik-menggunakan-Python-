import numpy as np
import matplotlib.pyplot as plt
index = np.arange(5)
values = [5,7,3,4,6]
plt.bar(index,values)
plt.xticks(index+0.4,['A','B','C','D','E'])
plt.show()
