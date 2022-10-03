import os
import socket
import time

# making a socket.
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind((socket.gethostname(), 21625))
skt.listen(5)
print("IP_address: ", skt.getsockname())

# establishing the connection.
peer, addr = skt.accept()
print("Connected !!!!")
# obtaining details of the apps.
app_name = input("App Name:")
app_size = os.path.getsize(app_name)

# Sending the name and details of the app.
peer.send(app_name.encode())
peer.send(str(app_size).encode())
# app data is encoded.
# sending app.
with open(app_name, "rb") as app:
    a = 0
    # time is recorded
    starting_time = time.time()

    #  loop is running  while a != file_size.
    while a <= app_size:
        packet = app.read(1024)
        if not (packet):
            break
        peer.sendall(packet)
        a += len(packet)

    ending_time = time.time()
    #time recording ended.

print("File Transfered successfully")
print("Total time: ", ending_time - starting_time)

skt.close()
#socket is closed