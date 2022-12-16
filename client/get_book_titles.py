import grpc

from inventory_client import InventoryServiceClient

"""
Module to fetch the book titles from the Inventory Service
"""


def get_book_titles(client: InventoryServiceClient, ISBN_list):
    titles = []
    """
    Method to get titles
    """
    for isbn in ISBN_list:
        # get the details of book from grpc client
        book_details = client.get_book_details(isbn)
        titles.append(book_details.title)
        print(titles)

    return titles


if __name__ == '__main__':
    localhost = 'localhost'
    port = 50051
    inventory_service_client = InventoryServiceClient(localhost, port)
    # calling the get_book_titles
    titles = get_book_titles(inventory_service_client, ['book1', 'book2'])
    # printing titles
    print(titles)
