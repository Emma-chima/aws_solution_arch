import stomp
import time
import ssl

# Listener to handle messages and errors
class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('Received an error:', frame.body)
    
    def on_message(self, frame):
        print('Received a message:', frame.body)

# ------------------------------
# Connection Setup
# ------------------------------
broker_host = "b-854dafca-d96f-4c2a-979d-020764281222-1.mq.eu-north-1.amazonaws.com"
broker_port = 61614

# Create connection
conn = stomp.Connection12([(broker_host, broker_port)])

# Correct way to enable SSL in stomp.py 8.2.0
conn.set_ssl(
    for_hosts=[(broker_host, broker_port)],
    ssl_version=ssl.PROTOCOL_TLSv1_2
)

# Add listener
conn.set_listener('', MyListener())

# ------------------------------
# Connect to the Broker
# ------------------------------
conn.connect(username="admin", passcode="Password123!", wait=True)

# ------------------------------
# Send and Receive
# ------------------------------
destination = "/queue/test"
conn.send(body="Hello, Amazon MQ!. Just testing the MQ service", destination=destination)

conn.subscribe(destination=destination, id=1, ack='auto')
time.sleep(2)  # Allow time to receive messages

# ------------------------------
# Disconnect
# ------------------------------

