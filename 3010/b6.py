import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
plt.title("a")
plt.xlabel("b")
plt.ylabel("c")
plt.hist(x,10)
plt.show()