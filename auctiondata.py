import bookauction as bau

def main():
    print("auctiondata.py")

def getBookTitles(books):
    options=[]
    for book in books:
        options.append(book.title)
    distinct_books=list(set(options))
    distinct_books.sort()
    return distinct_books

def getData():
    auction1 = bau.Bookauction("Moby Dick", "author1", "123", 5.50, "2025-05-01")
    auction2 = bau.Bookauction("Tom Sawyer", "author2", "456", 6.50, "2025-05-03")
    auction3 = bau.Bookauction("Little Women", "author3", "678", 18.50, "2025-05-08")
    auction4 = bau.Bookauction("A Tale of Two Cities", "author4", "111", 7.33, "2025-05-11")
    auction5 = bau.Bookauction("Little Women", "author3", "678", 4.50, "2025-05-08")
    auctionlist = [auction1, auction2, auction3, auction4, auction5]

    # dates = []
    # values = []
    #
    # for auction in auctionlist:
    #     dates.append(auction.sell_date)
    #     values.append(auction.sell_price)

    return auctionlist

if __name__ == '__main__':
    # main
    main()