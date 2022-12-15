# import required modules
from concurrent import futures
import grpc
import sys
sys.path.append("./service")
import service.inventoryModel_pb2 as inventoryModel_pb2
import service.inventoryModel_pb2_grpc as inventoryModel_pb2_grpc
import service.inventoryService_pb2 as inventoryService_pb2
import service.inventoryService_pb2_grpc as inventoryService_pb2_grpc


db = {
    'book1': {
        'isbn': 'book1',
        'title': 'The Notebook',
        'author': 'Nora Roberts',
        'genre': 'ROMANCE',
        'year': 1990
    },
    'book2': {
        'isbn': 'book2',
        'title': 'Last Wednesday',
        'author': 'Agatha Cristie',
        'genre': 'THRILLER',
        'year': 2009
    }
}

class InventoryServiceServicer (inventoryService_pb2_grpc.InventoryServiceServicer):

    def CreateBook(self, request, context):

        isbn = request.isbn
        title = request.title
        author = request.author
        genre = request.genre
        publishing_year = request.publishing_year 

        if isbn == "":
            responseStatus = inventoryModel_pb2.ResponseStatus(code = grpc.StatusCode.INVALID_ARGUMENT.value[0], message="Please enter valid ISBN")
            return inventoryService_pb2.CreateBookReply(statusCode=grpc.StatusCode.INVALID_ARGUMENT.value[0], response=responseStatus)

        if (isbn in db.keys()):
            responseStatus = inventoryModel_pb2.ResponseStatus(code = grpc.StatusCode.ALREADY_EXISTS.value[0], message="Duplicate ISBN exists")
            return inventoryService_pb2.CreateBookReply(statusCode=grpc.StatusCode.ALREADY_EXISTS.value[0], response=responseStatus)
    
        if title=="" or author=="":
            responseStatus = inventoryModel_pb2.ResponseStatus(code = grpc.StatusCode.INVALID_ARGUMENT.value[0], message="Title or Author missing!")
            return inventoryService_pb2.CreateBookReply(statusCode=grpc.StatusCode.INVALID_ARGUMENT.value[0], response=responseStatus)
        
        """All validations are successfull, go ahead to create book and add it to db"""
        bookToAdd = inventoryModel_pb2.Book(isbn = isbn, title=title, author=author, genre=genre, publishing_year=publishing_year)
        print(bookToAdd)
        db[isbn] = bookToAdd

        responseStatus = inventoryModel_pb2.ResponseStatus(code = grpc.StatusCode.OK.value[0], message="Book successfully created!")
        return inventoryService_pb2.CreateBookReply(statusCode= grpc.StatusCode.OK.value[0], responseStatus=responseStatus)