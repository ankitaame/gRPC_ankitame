"""
unit tests get_book_titles
"""
import unittest
from unittest import mock

from client.get_book_titles import get_book_titles
from client.inventory_client import InventoryServiceClient
from service.inventoryModel_pb2 import Book


class GetBookTitleMockTest(unittest.TestCase):
    """
    tests of get_book_tiles function using mock client
    """

    def setUp(self):
        """
         set up common fixtures
        """
        self.isbns = ['book1', 'book2']
        self.books = [Book(
            isbn='book1',
            title='Last Tuesday',
            author='Nora Mathur',
            genre='ROMANCE',
            publishing_year=1990
        ), Book(
            isbn='book2',
            title='Alex Rider',
            author='Anthony Horowitz',
            genre='ROMANCE',
            publishing_year=2022
        )]
        self.titles = ['Last Tuesday', 'Alex Rider']

    @mock.patch.object(InventoryServiceClient, 'get_book_details')
    def test_get_book_success(self, mock_get_book_details):
        """
          Return the expected book title with no errors
        """
        # set mocks
        mock_get_book_details.side_effect = self.books
        # create client
        client = InventoryServiceClient("test1", "test2")

        # test method
        actual_titles = get_book_titles(client, self.isbns)
        mock_get_book_details.call_count = len(self.isbns)
        expected_calls = [mock.call(self.isbns[0]), mock.call(self.isbns[1])]
        mock_get_book_details.assert_has_calls(expected_calls, any_order=False)
        # assert the output
        self.assertEqual(self.titles, actual_titles)

    @mock.patch.object(InventoryServiceClient, 'get_book_details')
    def test_get_book_title_some_book_not_found(self, get_book_details):
        """
                    Should return the book resultant_titles which are present and skip the absent ones
         """
        self.isbns = ['book1', 'book2']

        def side_effect(isbn: str):
            if isbn == self.isbns[0]:
                return self.books[0]
            elif isbn == self.isbns[1]:
                return self.books[1]

        get_book_details.side_effect = side_effect
        client = InventoryServiceClient("test", "test")

        resultant_titles = get_book_titles(client, self.isbns)

        expected = [mock.call(self.isbns[0]), mock.call(self.isbns[1])]

        get_book_details.assert_has_calls(expected, any_order=True)

        # verify output
        self.assertEqual(self.titles, resultant_titles)


class GetBookTitleLiveTest(unittest.TestCase):
    """
        Tests for get_book_title using live client
    """

    def setUp(self):
        """
                common fixtures
            """
        self.isbns_identifiers = ['book1', 'book2']
        self.titles = ['The Notebook', 'Last Wednesday']
        self.inventory_client = InventoryServiceClient("localhost", "50051")

    def test_get_book_title_success(self):
        """
            Test success
           """
        actual_titles = get_book_titles(self.inventory_client, self.isbns_identifiers)

        self.assertEqual(self.titles, actual_titles)

    def test_get_book_title_some_book_not_found(self):
        """
                 Test  book not found
                """
        self.isbns_identifiers = ['book1', 'book2']
        actual_titles = get_book_titles(self.inventory_client, self.isbns_identifiers)
        self.assertEqual(self.titles, actual_titles)
