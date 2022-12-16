# import required modules
from concurrent import futures
import grpc
import sys

sys.path.append("./service")
import service.inventoryModel_pb2 as inventoryModel_pb2
import service.inventoryModel_pb2_grpc as inventoryModel_pb2_grpc
import service.InventoryService_pb2 as inventoryService_pb2
import service.InventoryService_pb2_grpc as inventoryService_pb2_grpc

# pylint: disable=no-member
# Implemented the current database as a local memory hardcoded dictionary. This can be extended permanent storage

db = {
    'book1': {
        'isbn': 'book1',
        'title': 'The Notebook',
        'author': 'Nora Roberts',
        'genre': 'ROMANCE',
        'publishing_year': 1990
    },
    'book2': {
        'isbn': 'book2',
        'title': 'Last Wednesday',
        'author': 'Agatha Cristie',
        'genre': 'THRILLER',
        'publishing_year': 2009
    }
}


class InventoryServiceServicer(inventoryService_pb2_grpc.InventoryServiceServicer):
    """
               RPC Method to create a book in database after performing validation
               """

    def CreateBook(self, request, context):

        isbn = request.bookedCreated.isbn
        title = request.bookedCreated.title
        author = request.bookedCreated.author
        genre = request.bookedCreated.genre
        publishing_year = request.bookedCreated.publishing_year

        # isbn is empty or null
        if isbn == "":
            response_status = inventoryModel_pb2.ResponseStatus(code=grpc.StatusCode.INVALID_ARGUMENT.value[0],
                                                                message="Please enter valid ISBN")
            return inventoryService_pb2.CreateBookReply(statusCode=grpc.StatusCode.INVALID_ARGUMENT.value[0],
                                                        response=response_status)

        # isbn is present, will not add duplicate
        if (isbn in db.keys()):
            response_status = inventoryModel_pb2.ResponseStatus(code=grpc.StatusCode.ALREADY_EXISTS.value[0],
                                                                message="Duplicate ISBN exists! ")
            return inventoryService_pb2.CreateBookReply(statusCode=grpc.StatusCode.ALREADY_EXISTS.value[0],
                                                        response=response_status)

        # primary fields are empty .
        if title == "" or author == "":
            response_status = inventoryModel_pb2.ResponseStatus(code=grpc.StatusCode.INVALID_ARGUMENT.value[0],
                                                                message="Title or Author missing!")
            return inventoryService_pb2.CreateBookReply(statusCode=grpc.StatusCode.INVALID_ARGUMENT.value[0],
                                                        response=response_status)

        # isbn is successfully added and created
        book_to_add = inventoryModel_pb2.Book(isbn=isbn, title=title, author=author, genre=genre,
                                            publishing_year=publishing_year)

        db[isbn] = book_to_add

        # create success
        response_status = inventoryModel_pb2.ResponseStatus(code=grpc.StatusCode.OK.value[0],
                                                            message="Book successfully created!")
        return inventoryService_pb2.CreateBookReply(statusCode=grpc.StatusCode.OK.value[0], response=response_status)

    """
           RPC Method to Get a  book from the inventory
           """

    def GetBook(self, request, context):

        isbn = request.isbn
        # isbn is empty or null
        if isbn == "":
            responseStatus = inventoryModel_pb2.ResponseStatus(code=grpc.StatusCode.INVALID_ARGUMENT.value[0],
                                                               message="Please enter valid ISBN")
            return inventoryService_pb2.GetBookReply(statusCode=grpc.StatusCode.INVALID_ARGUMENT.value[0],
                                                     reponseMessage="Please enter valid ISBN", book={},
                                                     response=responseStatus)
        # isbn is does not exist in db
        if isbn not in db.keys():
            responseStatus = inventoryModel_pb2.ResponseStatus(code=grpc.StatusCode.INVALID_ARGUMENT.value[0],
                                                               message="Oops!! Book Not Found!!")
            return inventoryService_pb2.GetBookReply(statusCode=grpc.StatusCode.NOT_FOUND.value[0],
                                                     reponseMessage="Oops!! Book Not Found!!", book={},
                                                     response=responseStatus)

        requested_book = db[isbn]
        # book is available, then return details
        responseStatus = inventoryModel_pb2.ResponseStatus(code=grpc.StatusCode.INVALID_ARGUMENT.value[0],
                                                           message="Found the book")
        return inventoryService_pb2.GetBookReply(statusCode=grpc.StatusCode.OK.value[0], reponseMessage="Book found!",
                                                 book=requested_book, response=responseStatus)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    inventoryService_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryServiceServicer(), server)
    server.add_insecure_port('[::]:' + port)

    # start the server
    server.start()
    print("Server started, listening on " + port)

    server.wait_for_termination()


if __name__ == "__main__":
    # call serve method as soon as program runs
    serve()
