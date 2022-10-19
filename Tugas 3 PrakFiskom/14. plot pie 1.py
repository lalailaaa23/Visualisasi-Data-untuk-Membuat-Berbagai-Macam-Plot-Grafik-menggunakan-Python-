import numpy as np
import matplotlib.pyplot as plt
labels = ['Lain-lain','Samsung','Apple','Huawei','Oppo','Vivo']
values = [42,21,14,9,8,7]
colors = ['red','green','pink','blue','yellow','orange']
plt.pie(values,labels=labels,colors=colors)
plt.show()
