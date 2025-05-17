
import auctionwindow
import auctiondata as da


def main():
    #get data
    auction_data=da.getData()
    #create auction window
    auctionwindow.createWindow(auction_data)

if __name__ == '__main__':
    # main
    main()