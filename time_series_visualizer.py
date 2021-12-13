import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime as datetime
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

df = df[(df['value'] >= (df['value'].quantile(0.025))) &
        (df['value'] <= (df['value'].quantile(0.975)))]
print(df.count)

def draw_line_plot():
    df.plot.line()
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    plt.show()


def draw_bar_plot():
    df_copy = df.copy()
    df_copy['month'] = df_copy.index.month
    df_copy['year'] = df_copy.index.year
    df_copy_grouped = df_copy.groupby(["year", "month"])["value"].mean().unstack()

    axes = df_copy_grouped.plot.bar()
    axes.set_xlabel('Years')
    axes.set_ylabel('Average Page Views')
    axes.legend(
        labels=[datetime.datetime.strptime(str(d), "%m").strftime("%B") for d in sorted(df_copy.index.month.unique())])
    plt.show()

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box['month'] = pd.Categorical(df_box['month'], categories=months, ordered=True)
    df_box.sort_values(by=['month'])

    fig, (ax,ax2) = plt.subplots(ncols=2, sharey=True)
    fig.set_figwidth(20)
    fig.set_figheight(10)

    sns.boxplot(x=df_box['year'], y=df_box['value'], ax=ax).set(xlabel='Year', ylabel='Page Views')
    ax.set_title("Year-wise Box Plot (Trend)")

    sns.boxplot(x=df_box['month'], y=df_box['value'], ax=ax2).set(xlabel='Month', ylabel='Page Views')
    ax2.set_title("Month-wise Box Plot (Seasonality)")


    plt.show()

#draw_box_plot()
