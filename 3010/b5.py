import matplotlib.pyplot as plt
import numpy as np
firms = ["a","b","c","d","e"]
market_share = [20,25,15,10,5]
Explode = [0,0.1,0,0,0]
plt.pie(market_share,explode=Explode,labels=firms,shadow=True,startangle=45)
plt.axis('equal')
plt.legend(title="abcde")
plt.show()