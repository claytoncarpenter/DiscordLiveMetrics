import pandas as pd
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot():

    csv_path = r'C:\Users\clayt\Documents\Classicstron\Classicstron\document.csv'
    data = pd.read_csv(csv_path, delimiter='|')
    grouped_data = data.groupby(by='author').describe()
    print(grouped_data)
    print(grouped_data.index.to_numpy)
    print(grouped_data['content']['count'])

    # plt.style.use('fivethirtyeight')

    # x_values = []
    # y_values = []

    # index = count()



    data = pd.read_csv(csv_path, delimiter='|')
    grouped_data = data.groupby(by='author').describe()
    x_values = grouped_data.index
    y_values = grouped_data['content']['count']
    plt.bar(x_values, y_values)
    plt.xlabel('Author')
    plt.ylabel('Number of Comments')
    plt.title('Discord Posts')

    plt.show()

    return 'Hello from plot'
