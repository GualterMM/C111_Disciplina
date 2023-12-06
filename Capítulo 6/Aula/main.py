import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = x*2

y2 = x*x

plt.xlabel("Valores de X");
plt.ylabel("Valores de Y")
plt.plot(x, y, 'r--', x, y2, 'b--')
plt.show()