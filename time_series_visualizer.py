import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df[((df['value']>=df['value'].quantile(0.025) ) & (df['value']<=df['value'].quantile(0.975)))]


def draw_line_plot():
    # Draw line plot
    fig,ax=plt.subplots()
    ax.plot(df['date'],df['value'])
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    db=df.copy()
    fig,ax=plt.subplots()
    db['date']=pd.to_datetime(db['date'])
    db['month']=db['date'].dt.strftime('%B')
    db['year']=db['date'].dt.year
    bar=db.groupby(['year','month'])['value'].mean().reset_index()
    pivot_table = bar.pivot(index='year', columns='month', values='value')
    pivot_table = pivot_table[['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']]
    pivot_table.plot(kind="bar",ax=ax,figsize=(12,8))
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', bbox_to_anchor=(1.05, 1), loc='upper left')
    fig.tight_layout()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box['date'] = pd.to_datetime(df_box['date'])
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')  # Short month names

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2, figsize=(14, 7))

    # Year-wise Box Plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axs[0])
    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')

    # Month-wise Box Plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axs[1])
    axs[1].set_title('Month-wise Box Plot (Seasonality)')
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')

    # Rotate x-tick labels for the month-wise plot
    plt.setp(axs[1].xaxis.get_majorticklabels(), rotation=45)

    # Adjust layout
    fig.tight_layout()

    # Save and return figure
    fig.savefig('box_plot.png')
    return fig
