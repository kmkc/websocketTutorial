import sys
from websocket import create_connection

ws = create_connection('ws://www.hogehoge.xyz:3000/websocket')

if len(sys.argv) > 1:
    message = sys.argv[1]
else:
    message = 'hello'

print ws.send(message)
print ws.recv()

ws.close()
