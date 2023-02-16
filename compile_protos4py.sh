rm -rf ./python/protos
protoc -I=./common --python_out=./python/protos --pyi_out=./python/protos  ./common/communication.proto