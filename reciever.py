import os
import socket
import time

ads = input("IP_address: ")
# making a socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting to the socket.
try:
    skt.connect((ads, 21625))
    print("Connected !!!!")
except:
    print("connection error!!!!!")
    exit(0)

# Sending the details of the app.
app_name = skt.recv(100).decode()
app_size = skt.recv(100).decode()

# Opening and then reading the file.
with open("./down/" + app_name, "wb") as app:
    a = 0
    #time capturing starts
    starting_time = time.time()

    # Running the loop and calculating the time.
    while a <= int(app_size):
        packet = skt.recv(1024)
        if not (packet):
  



            break
        app.write(packet)
        a += len(packet)


    ending_time = time.time()
    # time capture ends.

print("File Transfered successfully")
print("Total time: ", ending_time - starting_time)

skt.close()

#socket closed