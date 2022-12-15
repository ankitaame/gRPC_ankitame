import inventoryModel_pb2 as _inventoryModel_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBookReply(_message.Message):
    __slots__ = ["response", "statusCode"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    response: _inventoryModel_pb2.ResponseStatus
    statusCode: int
    def __init__(self, statusCode: _Optional[int] = ..., response: _Optional[_Union[_inventoryModel_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class CreateBookRequest(_message.Message):
    __slots__ = ["bookedCreated"]
    BOOKEDCREATED_FIELD_NUMBER: _ClassVar[int]
    bookedCreated: _inventoryModel_pb2.Book
    def __init__(self, bookedCreated: _Optional[_Union[_inventoryModel_pb2.Book, _Mapping]] = ...) -> None: ...

class GetBookReply(_message.Message):
    __slots__ = ["book", "reponseMessage", "response", "statusCode"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    REPONSEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    book: _inventoryModel_pb2.Book
    reponseMessage: str
    response: _inventoryModel_pb2.ResponseStatus
    statusCode: int
    def __init__(self, statusCode: _Optional[int] = ..., reponseMessage: _Optional[str] = ..., book: _Optional[_Union[_inventoryModel_pb2.Book, _Mapping]] = ..., response: _Optional[_Union[_inventoryModel_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...
