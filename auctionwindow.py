import tkinter as tk
import auctionplot
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import bookauction as bau


def selectBook():
    print("book selected")

def main():
    print("auction window")

def createWindow(dt,book_options):

    # Create the main window
    window = tk.Tk()

    # Set the title of the window
    window.title("Auction Activity")

    # Set the size of the window (optional)
    window.geometry("500x500")

    frame = tk.Frame(window)
    frame.pack()

    label = tk.Label(frame, text="Auction Activity")


    selected_option=tk.StringVar(window)
    #selected_option.set("select")
    options = book_options
    #options = ["option 1", "option 2", "option 3"]
    dropdown = tk.OptionMenu(window, selected_option, *options)
    dropdown.pack()

    button = tk.Button(window, text="My Button",command=lambda:selectBook())
    button.pack()

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

    dates = []
    values = []

    for auction in dt:
        dates.append(auction.sell_date)
        values.append(auction.sell_price)

    fig=auctionplot.plotAuctionData(dates, values)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == '__main__':
    # main
    main()