from obsolete import book_auction as bau


def main():
    print("auction_data.py")

def get_book_titles(books):
    options=[]
    for book in books:
        options.append(book.title)
    distinct_books=list(set(options))
    distinct_books.sort()
    distinct_books.insert(0,"Select Book")
    return distinct_books


def get_data():
    auction1 = bau.BookAuction("Moby Dick", "author1", "123", 5.50, "2025-05-01")
    auction2 = bau.BookAuction("Tom Sawyer", "author2", "456", 6.50, "2025-05-03")
    auction3 = bau.BookAuction("Little Women", "author3", "678", 18.50, "2025-05-08")
    auction4 = bau.BookAuction("A Tale of Two Cities", "author4", "111", 7.33, "2025-05-11")
    auction5 = bau.BookAuction("Little Women", "author3", "678", 4.50, "2025-06-08")
    auction6 = bau.BookAuction("Tom Sawyer", "author2", "456", 21.50, "2025-06-13")
    auction7 = bau.BookAuction("Little Women", "author3", "678", 41.50, "2025-08-18")
    auctionlist = [auction1, auction2, auction3, auction4, auction5, auction6,auction7]

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