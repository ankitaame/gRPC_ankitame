from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

AVAILABLE: IssueStatus
DESCRIPTOR: _descriptor.FileDescriptor
NON_FICTION: Genre
ROMANCE: Genre
TAKEN: IssueStatus
THRILLER: Genre

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "publishing_year", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHING_YEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Genre
    isbn: str
    publishing_year: int
    title: str
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Genre, str]] = ..., publishing_year: _Optional[int] = ...) -> None: ...

class CreateBookReply(_message.Message):
    __slots__ = ["response", "statusCode"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    response: ResponseStatus
    statusCode: int
    def __init__(self, statusCode: _Optional[int] = ..., response: _Optional[_Union[ResponseStatus, _Mapping]] = ...) -> None: ...

class CreateBookRequest(_message.Message):
    __slots__ = ["bookedCreated"]
    BOOKEDCREATED_FIELD_NUMBER: _ClassVar[int]
    bookedCreated: Book
    def __init__(self, bookedCreated: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class GetBookReply(_message.Message):
    __slots__ = ["book", "reponseMessage", "response", "statusCode"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    REPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    book: Book
    reponseMessage: str
    response: ResponseStatus
    statusCode: int
    def __init__(self, statusCode: _Optional[int] = ..., reponseMessage: _Optional[str] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., response: _Optional[_Union[ResponseStatus, _Mapping]] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["book", "inventory_number", "status"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    book: Book
    inventory_number: int
    status: IssueStatus
    def __init__(self, inventory_number: _Optional[int] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[IssueStatus, str]] = ...) -> None: ...

class ResponseStatus(_message.Message):
    __slots__ = ["code", "message"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class IssueStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
