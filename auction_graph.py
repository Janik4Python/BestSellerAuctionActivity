import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
from datetime import datetime
from matplotlib.figure import Figure
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

    # Clear previous plot
    a.cla()
    a.set_axis_on()

    # Add x-axis label
    a.set_xlabel("Date")
    # Add y-axis label
    a.set_ylabel("Cost")

    # Redraw plot with updated data
    a.scatter(x_data, y_data)

    # Update the canvas
    canvas.draw()

# Create Tkinter window
window = tk.Tk()
window.configure(bg="white")
window.geometry("500x500")
window.title("Book Auctions")

top= tk.Frame(window)
top.configure(background="white")
top.configure(height=100)
bottom = tk.Frame(window)
bottom.configure(background="white")

top.pack(side="top", pady=20)
bottom.pack(side="bottom", expand=True)

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
f = Figure(figsize=(4,4), dpi=100)
a = f.add_subplot()
a.scatter([],[])
a.set_axis_off()

# Embed Matplotlib figure in Tkinter canvas
canvas = FigureCanvasTkAgg(f, master=window)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Run Tkinter event loop
window.mainloop()