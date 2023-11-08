import socket

HOST = "localhost"  # Change this to the server's IP address if it's not localhost
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected with server at {HOST}:{PORT}")

    while True:
        message = input("Enter a string: ")
        if message == "Stop":
            break

        s.sendall(message.encode('utf-8'))
        response = s.recv(1024).decode('utf-8')
        print(f"Received response from server: {response}")
