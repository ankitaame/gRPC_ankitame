## Protocol buffer generation:

`
python3 -m grpc_tools.protoc -I./protos protos/* --python_out=./service --grpc_python_out=./service --pyi_out=./service
`

##  gRPC server:

`python3 server.py`

