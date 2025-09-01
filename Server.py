import localchat
import time
localchat.initialize(port = 6666,format = 'utf-8', disconnect_msg = 'Déconecté')
localchat.start_server()
while True:
    time.sleep(1)
