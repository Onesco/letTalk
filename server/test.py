import time
from connect_client import Client

c1 = Client('Onesmus')
time.sleep(0.1)
c1.send_message("good evening guys")
time.sleep(0.1)
c1.send_message("how far")
time.sleep(2)
# c1.send_message("{quit}")
c2 = Client('Santos')
time.sleep(0.1)
c2.send_message("good evening guys")
time.sleep(0.1)
c2.send_message("what is up")
time.sleep(2)