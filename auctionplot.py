import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.figure import Figure
import pandas as pd
from datetime import datetime

def plotAuctionData():
# Sample data
    dates = ['2025-05-01', '2025-05-08', '2025-05-15', '2025-05-22', '2025-05-29']
    values = [10, 15, 7, 12, 9]

    # Convert dates to datetime objects
    dates = [pd.to_datetime(d) for d in dates]

    # Create the scatter plot
    plt.figure(figsize=(10, 6)) # Adjust figure size as needed
    plt.scatter(dates, values)

    # Format the x-axis to show dates nicely
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7)) # Show ticks every 7 days
    plt.gcf().autofmt_xdate() # Rotate date labels for better readability

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Scatter Plot with Datetime on X-axis')

    fig = plt.gcf()
    return fig



    return plt







def auctionplot():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [5, 6, 7, 8]) # Example plot
    return fig


