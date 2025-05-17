import tkinter as tk
import auctionplot
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def selectBook():
    print("book selected")

def main():
    print("auction window")

def createWindow(dt):

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
    selected_option.set("select")
    options = dt
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

    fig=auctionplot.plotAuctionData()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == '__main__':
    # main
    main()