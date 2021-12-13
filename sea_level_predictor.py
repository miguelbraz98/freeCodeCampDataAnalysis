import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.5)

    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    xA = np.arange(df['Year'].min(), 2050, 1)
    yA = xA * line1.slope + line1.intercept
    plt.plot(xA, yA)

    df_sliced = df.copy()
    df_sliced = df_sliced[df_sliced['Year'] >= 2000]

    line2 = linregress(df_sliced['Year'], df_sliced['CSIRO Adjusted Sea Level'])
    xB = np.arange(2000, 2050, 1)
    yB = xB * line2.slope + line2.intercept
    plt.plot(xB, yB)

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.show()




draw_plot()