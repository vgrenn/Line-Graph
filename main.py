import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('movie_info.csv')

x = df['Title']
y = df['Ratings']

plt.xlabel('Titles', fontsize=18)
plt.ylabel('Ratings', fontsize=16)
plt.plot(x,y)

plt.show()
