# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: InventoryService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16InventoryService.proto\x12\tinventory\"\xc2\x01\n\x04\x42ook\x12\x11\n\x04isbn\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05title\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06\x61uthor\x18\x03 \x01(\tH\x02\x88\x01\x01\x12$\n\x05genre\x18\x04 \x01(\x0e\x32\x10.inventory.GenreH\x03\x88\x01\x01\x12\x1c\n\x0fpublishing_year\x18\x05 \x01(\x05H\x04\x88\x01\x01\x42\x07\n\x05_isbnB\x08\n\x06_titleB\t\n\x07_authorB\x08\n\x06_genreB\x12\n\x10_publishing_year\"\xa4\x01\n\rInventoryItem\x12\x1d\n\x10inventory_number\x18\x01 \x01(\x05H\x01\x88\x01\x01\x12\x1f\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x0f.inventory.BookH\x00\x12+\n\x06status\x18\x03 \x01(\x0e\x32\x16.inventory.IssueStatusH\x02\x88\x01\x01\x42\x06\n\x04itemB\x13\n\x11_inventory_numberB\t\n\x07_status\"N\n\x0eResponseStatus\x12\x11\n\x04\x63ode\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05_codeB\n\n\x08_message\"R\n\x11\x43reateBookRequest\x12+\n\rbookedCreated\x18\x01 \x01(\x0b\x32\x0f.inventory.BookH\x00\x88\x01\x01\x42\x10\n\x0e_bookedCreated\"R\n\x0f\x43reateBookReply\x12\x12\n\nstatusCode\x18\x01 \x01(\x05\x12+\n\x08response\x18\x02 \x01(\x0b\x32\x19.inventory.ResponseStatus\"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"\x86\x01\n\x0cGetBookReply\x12\x12\n\nstatusCode\x18\x01 \x01(\x05\x12\x16\n\x0ereponseMessage\x18\x02 \x01(\t\x12\x1d\n\x04\x62ook\x18\x03 \x01(\x0b\x32\x0f.inventory.Book\x12+\n\x08response\x18\x04 \x01(\x0b\x32\x19.inventory.ResponseStatus*3\n\x05Genre\x12\x0b\n\x07ROMANCE\x10\x00\x12\x0f\n\x0bNON_FICTION\x10\x01\x12\x0c\n\x08THRILLER\x10\x02*\'\n\x0bIssueStatus\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x32\x9d\x01\n\x10InventoryService\x12H\n\nCreateBook\x12\x1c.inventory.CreateBookRequest\x1a\x1a.inventory.CreateBookReply\"\x00\x12?\n\x07GetBook\x12\x19.inventory.GetBookRequest\x1a\x17.inventory.GetBookReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'InventoryService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENRE._serialized_start=818
  _GENRE._serialized_end=869
  _ISSUESTATUS._serialized_start=871
  _ISSUESTATUS._serialized_end=910
  _BOOK._serialized_start=38
  _BOOK._serialized_end=232
  _INVENTORYITEM._serialized_start=235
  _INVENTORYITEM._serialized_end=399
  _RESPONSESTATUS._serialized_start=401
  _RESPONSESTATUS._serialized_end=479
  _CREATEBOOKREQUEST._serialized_start=481
  _CREATEBOOKREQUEST._serialized_end=563
  _CREATEBOOKREPLY._serialized_start=565
  _CREATEBOOKREPLY._serialized_end=647
  _GETBOOKREQUEST._serialized_start=649
  _GETBOOKREQUEST._serialized_end=679
  _GETBOOKREPLY._serialized_start=682
  _GETBOOKREPLY._serialized_end=816
  _INVENTORYSERVICE._serialized_start=913
  _INVENTORYSERVICE._serialized_end=1070
# @@protoc_insertion_point(module_scope)