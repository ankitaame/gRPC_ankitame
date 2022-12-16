import grpc
import sys
import sys

import grpc

sys.path.append("../service")
from service.InventoryService_pb2_grpc import InventoryServiceStub
from service.InventoryService_pb2 import GetBookRequest


# pylint: disable=no-member

class InventoryServiceClient:

    def __init__(self, server_address, server_port) -> None:
        self.server_address = server_address
        self.server_port = server_port
        self.channel = grpc.insecure_channel(server_address + ':' + str(server_port))
        self.stub = InventoryServiceStub(self.channel)
        print("Client initialization completed!!!")

    def get_book_details(self, isbn):
        """
        Method to get details of the book with given isbn
        :param isbn: string.
        :return: Book object defined in the protocol buffers
        """
        try:
            print("Getting data from server for" + isbn)
            book_req = GetBookRequest(isbn=isbn)
            get_book_resp = self.stub.GetBook(book_req)
        except grpc.RpcError as err:
            print("gRPC ERROR: [" + err.code().name + "]: Not Possible to fetch data for ISBN: " + isbn)
        else:
            print("Fetched data " + isbn)
            print(get_book_resp.book)
            return get_book_resp.book
