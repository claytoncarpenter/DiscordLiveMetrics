import pandas as pd
import random
from itertools import count
import matplotlib.pyplot as plt

def plot():

    csv_path = r'C:\Users\clayt\Documents\Classicstron\Classicstron\document.csv'
    data = pd.read_csv(csv_path, delimiter='|')
    grouped_data = data.groupby(by='author').describe()


    # plt.style.use('fivethirtyeight')

    # x_values = []
    # y_values = []

    # index = count()


    fig = plt.figure()
    fig.set_size_inches(15,15)
    data = pd.read_csv(csv_path, delimiter='|')
    grouped_data = data.groupby(by='author').describe()
    x_values = grouped_data.index
    y_values = grouped_data['content']['count']
    plt.bar(x_values, y_values)
    plt.xlabel('Author')
    plt.ylabel('Number of Comments')
    plt.title('Discord Posts')
    plt.xticks(rotation = 45)

    fig.savefig(r'static\plot.png')
    pass
