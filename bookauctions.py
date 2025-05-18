
import auctionwindow
import auctiondata as da


def main():
    #get data
    auction_data=da.getData()
    book_list=da.getBookTitles(auction_data)

    #create auction window
    auctionwindow.createWindow(auction_data,book_list)

if __name__ == '__main__':
    # main
    main()