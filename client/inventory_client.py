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
            try:
                print("Getting data from server for" + isbn)
                bookReq = GetBookRequest(isbn=isbn)
                bookResp = self.stub.GetBook(bookReq)
            except grpc.RpcError as err:
                print("gRPC ERROR: [" + err.code().name + "]: Couldn't fetch data for ISBN: " + isbn + " from gRPC Server..")
            else:
                print("Fetched data for ISBN: " + isbn + " from gRPC Server..")
                print(bookResp.book)
                return bookResp.book