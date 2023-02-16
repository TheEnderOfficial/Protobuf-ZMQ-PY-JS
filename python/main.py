import zmq
import protos.communication_pb2 as root

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:3000")

#  Do 10 requests, waiting each time for a response
for request in range(1):
    print("Sending request %s …" % request)
    msg = root.AwesomeMessage()
    msg.awesome_field = "hello, world!"
    socket.send(msg.SerializeToString())

    #  Get the reply.
    message = socket.recv()
    pMsg = root.AwesomeMessage.FromString(message)
    print(pMsg.awesome_field)