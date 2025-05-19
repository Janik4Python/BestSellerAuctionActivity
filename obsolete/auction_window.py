import tkinter as tk
from obsolete import auction_plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def main():
    print("auction window")

def create_window(dt,book_options):



    # Create the main window
    window = tk.Tk()

    # Set the title of the window
    window.title("Auction Activity")

    # Set the size of the window (optional)
    window.geometry("500x500")

    frame = tk.Frame(window)
    frame.pack()
    label = tk.Label(frame, text="Auction Activity")

    selected_value=tk.StringVar(window)
    options = book_options
    selected_value.set(options[0])
    dropdown = tk.OptionMenu(window, selected_value, *options)
    dropdown.pack()

    button = tk.Button(window, text="Show Graph",command=lambda:select_book(selected_value.get()))
    button.pack()

    canvas = tk.Canvas(window, width=200, height=200,bg="white")
    canvas.pack()

    def select_book(book_title):
        dates = []
        values = []
        for auction in dt:
            if auction.title == book_title:
                dates.append(auction.sell_date)
                values.append(auction.sell_price)


        fig = auction_plot.plot_auction_data(book_title, dates, values)
        graph_canvas = FigureCanvasTkAgg(fig, master=window)
        canvas_widget = graph_canvas.get_tk_widget()
        canvas_widget.pack()

    # graphic window
    # image_path = "graph-here.jpg"  # Replace with the actual path to your image
    # try:
    #     image = Image.open(image_path)
    #     # Resize the image if needed
    #     image = image.resize((400, 400))
    #     # Convert the image to Tkinter PhotoImage format
    #     photo = ImageTk.PhotoImage(image)
    #
    #     # Create a Label widget to display the image
    #     image_label = tk.Label(window, image=photo)
    #     image_label.pack()
    #
    #     # Keep a reference to the image to prevent garbage collection
    #     image_label.image = photo
    #
    # except FileNotFoundError:
    #     # Handle the case where the image file is not found
    #     error_label = tk.Label(window, text="Error: Image file not found.")
    #     error_label.pack()

    #plot in window
    # Sample data
    #     dates = ['2025-05-01', '2025-05-08', '2025-05-15', '2025-05-22', '2025-05-29']
    #     values = [10, 15, 7, 12, 9]

    # auction1 = bau.Bookauction("title1", "author1", "123", 5.50, "2025-05-01")
    # auction2 = bau.Bookauction("title2", "author2", "456", 6.50, "2025-05-03")
    # auction3 = bau.Bookauction("title3", "author3", "678", 18.50, "2025-05-08")
    # auction4 = bau.Bookauction("title4", "author4", "111", 7.33, "2025-05-11")
    # auctionlist = [auction1, auction2, auction3, auction4]

    # dates = []
    # values = []
    #
    # for auction in dt:
    #     dates.append(auction.sell_date)
    #     values.append(auction.sell_price)
    #
    # fig=auction_plot.plot_auction_data(dates, values)
    # canvas = FigureCanvasTkAgg(fig, master=window)
    # canvas_widget = canvas.get_tk_widget()
    # canvas_widget.pack()

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == '__main__':
    # main
    main()