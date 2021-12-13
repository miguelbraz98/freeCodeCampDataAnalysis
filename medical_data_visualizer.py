import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('medical_examination.csv')
df['overweight'] = np.where((df['weight'] / ((df['height'] / 100) ** 2)) > 25, 1, 0)
df['cholesterol'] = np.where(df['cholesterol'] >= 2, 1, 0)
df['gluc'] = np.where(df['gluc'] >= 2, 1, 0)

def medical():

    formatted = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    #plt.ylabel('total')
    plot = sns.catplot(data=formatted, kind="count",  x="variable", hue="value", col="cardio").set_axis_labels("variable", "total")
    plt.show()
    return plot

def heat():
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= (df['height'].quantile(0.025))) &
                 (df['height'] <= (df['height'].quantile(0.975))) &
                 (df['weight'] >= (df['weight'].quantile(0.025))) &
                 (df['weight'] <= (df['weight'].quantile(0.975)))]

    corr = df_heat.corr()
    mask = np.triu(corr)
    fig, ax = plt.subplots(figsize=(9,9))

    sns.heatmap(corr, annot=True, fmt='.1f', linewidths=1, mask=mask, vmax=.8, center=0.09, square=True)

    plt.show()


heat()

