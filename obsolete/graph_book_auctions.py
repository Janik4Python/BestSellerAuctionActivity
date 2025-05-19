from obsolete import auction_window
import auction_data as da

def main():
    #get data
    auction_data=da.get_data()
    book_list=da.get_book_titles(auction_data)

    #create auction window
    auction_window.create_window(auction_data, book_list)

if __name__ == '__main__':
    # main
    main()