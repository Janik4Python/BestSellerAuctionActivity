import tkinter as tk

def main():

    # Create the main window
    window = tk.Tk()

    # Set the title of the window
    window.title("Auction Activity")

    # Set the size of the window (optional)
    window.geometry("500x500")

    button = tk.Button(window, text="My Button", background="red")
    button.pack()

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == '__main__':
    # main
    main()