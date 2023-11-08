import socket
import re

HOST = "localhost"  # Change this to the server's IP address if it's not localhost
PORT = 5000

def palindrome_check(string):
    if string == string[::-1]:
        return True
    else:
        return False

def vowel_count(string):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in string:
        if char in vowels:
            vowels[char] += 1
    return vowels

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        client_socket, address = s.accept()
        print(f"Connected with client at {address}")

        while True:
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Received data from client: {data}")

            if data == "Stop":
                break

            is_palindrome = palindrome_check(data)
            vowel_counts = vowel_count(data)

            response = f"Is palindrome: {is_palindrome}, Length: {len(data)}, Vowel counts: {vowel_counts}"
            client_socket.sendall(response.encode('utf-8'))

        client_socket.close()
        print("Client disconnected")
