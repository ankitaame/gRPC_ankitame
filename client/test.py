"""
Module to unit test the get_book_titles method using mocks
"""
import unittest
from unittest import mock

from client.get_book_titles import get_book_titles
from client.inventory_client import InventoryServiceClient
from service.inventoryModel_pb2 import Book

class GetBookTitleUsingMockTestCase(unittest.TestCase):
 
    def setUp(self):
    
        self.isbns = ['book1', 'book2']
        self.books = [Book(
            isbn='book1',
            title='Mock Tripwire',
            author='Lee Child',
            genre='ROMANCE',
            publishing_year=1987
        ), Book(
            isbn='book3',
            title='Mock Egyptian Civilization',
            author='Mike Henry',
            genre='ROMANCE',
            publishing_year=1960
        )]
        self.titles = ['Mock Tripwire', 'Mock Egyptian Civilization']

    @mock.patch.object(InventoryServiceClient, 'get_book_details')
    def test_get_book_title_no_error(self, mock_grpc_get_book_details):
        
        mock_grpc_get_book_details.side_effect = self.books

        # creating the client with mocked method
        inventory_client = InventoryServiceClient("test", "test")

        # calling the method to test
        actual_titles = get_book_titles(inventory_client, self.isbns)

        # performing the verification
        mock_grpc_get_book_details.call_count = len(self.isbns)
        # specifying expected calls for the method
        expected_calls = [mock.call(self.isbns[0]), mock.call(self.isbns[1])]
        # verifying the calls are made as per specific order
        mock_grpc_get_book_details.assert_has_calls(expected_calls, any_order=False)

        # verifying the output
        self.assertEqual(self.titles, actual_titles, "The titles are not as expected.")

    @mock.patch.object(InventoryServiceClient, 'get_book_details')
    def test_get_book_title_some_book_not_found(self, mock_grpc_get_book_details):

        self.isbns = ['book1', 'book2']

        def side_effect(isbn: str):
            if isbn == self.isbns[0]:
                return self.books[0]
            elif isbn == self.isbns[1]:
                return self.books[1]


        mock_grpc_get_book_details.side_effect = side_effect
        inventory_client = InventoryServiceClient("test","test")

        actual_titles = get_book_titles(inventory_client, self.isbns)

        mock_grpc_get_book_details.call_count = len(self.isbns)

        expected_calls = [mock.call(self.isbns[0]), mock.call(self.isbns[1])]

        mock_grpc_get_book_details.assert_has_calls(expected_calls, any_order=True)

        self.assertEqual(self.titles, actual_titles, "The titles are not as expected.")

class GetBookTitleUsingLiveTestCase(unittest.TestCase):


    def setUp(self):

        self.isbns = ['book1', 'book2']
        self.titles = ['The Notebook', 'Last Wednesday']
        self.inventory_client = InventoryServiceClient("localhost", "50051")

    def test_get_book_title_no_error(self):

        actual_titles = get_book_titles(self.inventory_client, self.isbns)

        self.assertEqual(self.titles, actual_titles, "The titles are not as expected.")

    def test_get_book_title_some_book_not_found(self):

        self.isbns = ['book1', 'book2']
        actual_titles = get_book_titles(self.inventory_client, self.isbns)
        self.assertEqual(self.titles, actual_titles, "The titles are not as expected.")


