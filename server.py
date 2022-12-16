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


class InventoryServiceServicer (inventoryService_pb2_grpc.InventoryServiceServicer):

    def CreateBook(self, request, context):

        isbn = request.bookedCreated.isbn
        title = request.bookedCreated.title
        author = request.bookedCreated.author
        genre = request.bookedCreated.genre
        publishing_year = request.bookedCreated.publishing_year 
        print(isbn,title, author, genre,publishing_year)
        if isbn == "":
            responseStatus = inventoryModel_pb2.ResponseStatus(code = grpc.StatusCode.INVALID_ARGUMENT.value[0], message="Please enter valid ISBN")
            return inventoryService_pb2.CreateBookReply(statusCode=grpc.StatusCode.INVALID_ARGUMENT.value[0], response=responseStatus)

        if (isbn in db.keys()):
            responseStatus = inventoryModel_pb2.ResponseStatus(code = grpc.StatusCode.ALREADY_EXISTS.value[0], message="Duplicate ISBN exists")
            return inventoryService_pb2.CreateBookReply(statusCode=grpc.StatusCode.ALREADY_EXISTS.value[0], response=responseStatus)
    
        if title=="" or author=="":
            responseStatus = inventoryModel_pb2.ResponseStatus(code = grpc.StatusCode.INVALID_ARGUMENT.value[0], message="Title or Author missing!")
            return inventoryService_pb2.CreateBookReply(statusCode=grpc.StatusCode.INVALID_ARGUMENT.value[0], response=responseStatus)
        

        bookToAdd = inventoryModel_pb2.Book(isbn = isbn, title=title, author=author, genre=genre, publishing_year=publishing_year)
        print(bookToAdd)
        db[isbn] = bookToAdd

        responseStatus = inventoryModel_pb2.ResponseStatus(code = grpc.StatusCode.OK.value[0], message="Book successfully created!")
        return inventoryService_pb2.CreateBookReply(statusCode= grpc.StatusCode.OK.value[0], response=responseStatus)


    def GetBook(self, request, context):

        isbn = request.isbn
       
        if isbn == "":
           responseStatus = inventoryModel_pb2.ResponseStatus(code = grpc.StatusCode.INVALID_ARGUMENT.value[0], message="Please enter valid ISBN")
           return inventoryService_pb2.GetBookReply(statusCode=grpc.StatusCode.INVALID_ARGUMENT.value[0], reponseMessage="Please enter valid ISBN",book={}, response=responseStatus)

        if (isbn not in db.keys()):
           
           responseStatus = inventoryModel_pb2.ResponseStatus(code = grpc.StatusCode.INVALID_ARGUMENT.value[0], message="Oops!! Book Not Found!!")
           return inventoryService_pb2.GetBookReply(statusCode=grpc.StatusCode.NOT_FOUND.value[0], reponseMessage="Oops!! Book Not Found!!",book={}, response=responseStatus)

    
        requestedBook = db[isbn]

        responseStatus = inventoryModel_pb2.ResponseStatus(code = grpc.StatusCode.INVALID_ARGUMENT.value[0], message="Found the book")
        return inventoryService_pb2.GetBookReply(statusCode=grpc.StatusCode.OK.value[0], reponseMessage="Book found!",book=requestedBook, response=responseStatus)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    inventoryService_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryServiceServicer(), server)
    server.add_insecure_port('[::]:' + port)

    # start the server 
    server.start()
    print("Server started, listening on " + port)

    # wait for termination
    server.wait_for_termination()


if __name__ == "__main__":
    # call serve method as soon as program runs
    serve()