import tkinter as tk

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import pandas as pd

import auction_data as da

# Initialize data
auction_data = da.get_data()
book_list = da.get_book_titles(auction_data)

# Function to update data and redraw plot
def update_plot(selected_book):

    x_data=[]
    y_data=[]

    for auction in auction_data:
        if auction.title == selected_book:
            x_data.append(auction.sell_date)
            y_data.append(auction.sell_price)

    # Convert dates to datetime objects
    x_data = [pd.to_datetime(d) for d in x_data]

    # Clear previous plot
    axis.cla()
    axis.set_axis_on()

    # Format the x-axis to show dates nicely
    axis.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    figure.autofmt_xdate() # Rotate date labels for better readability
    formatter = ticker.StrMethodFormatter('${x:,.2f}')
    axis.yaxis.set_major_formatter(formatter)
    axis.yaxis.set_label_coords(-0.125, 0.5)
    axis.xaxis.set_label_coords(0.5, -0.255)

    # Add x-axis label
    axis.set_xlabel("Date")
    # Add y-axis label
    axis.set_ylabel("Cost")
    # Add grid
    axis.grid(True)

    # Redraw plot with updated data
    axis.scatter(x_data, y_data)

    # Update the canvas
    canvas.draw()

# Create Tkinter window
window = tk.Tk()
window.configure(bg="white")
window.geometry("800x800")
window.title("Book Auctions")

top= tk.Frame(window)
top.configure(background="white")
top.configure(height=50)
bottom = tk.Frame(window)
bottom.configure(background="white")

top.pack(side="top", pady=20)
bottom.pack(side="top")

#book dropdown
selected_value = tk.StringVar(window)
selected_value.set(book_list[0])
dropdown = tk.OptionMenu(window, selected_value, *book_list)
dropdown.configure(bg="white")
dropdown.pack(in_=top, side="left")

#graph button
button = tk.Button(window, text="Graph", command=lambda:update_plot(selected_value.get()), highlightbackground='white')
button.pack(in_=top, side="left")

#blank graph
figure = Figure(figsize=(6.5,4), dpi=100)
axis = figure.add_subplot()
axis.scatter([],[])
axis.set_axis_off()

# Embed Matplotlib figure in Tkinter canvas
canvas = FigureCanvasTkAgg(figure, master=bottom)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Run Tkinter event loop
window.mainloop()