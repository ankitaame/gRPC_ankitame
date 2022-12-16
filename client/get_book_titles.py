import grpc

from inventory_client import InventoryServiceClient

def get_book_titles(client: InventoryServiceClient, isbn_list):
    titles = []

    for isbn in isbn_list:
            book_details = client.get_book_details(isbn)
            titles.append(book_details.title)
            print(titles)

    return titles

if __name__ == '__main__':
    localhost = 'localhost'
    port = 50051
    inventory_service_client = InventoryServiceClient(localhost, port)

    titles = get_book_titles(inventory_service_client, ['book1', 'book2'])

    print(titles)
