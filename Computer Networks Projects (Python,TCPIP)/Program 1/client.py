#Program 1
#client.py
#CSCI 4760
#Jacob Maraffi
#811-571-598
import socket
import sys
import pickle

#creating the client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connection the clientSocket to the server
serverName = 'localhost'
serverPort = 8080
clientName = 'Client of Jacob'
clientSocket.connect((serverName, serverPort))

#accepting input from the keybaord (integer)
number = input('Input an integer between 0 and 100:')
data = pickle.dumps({0: clientName, 1: number})

#encoding the data and sending it to the server
clientSocket.send(data)

#recieving the new data back from the server
newData = clientSocket.recv(1024)
newData = pickle.loads(newData)

#printing the results
print("Name from server:", newData.get(0))
print("Number from server:", newData.get(1))
print("Random Number generated by the server:", newData.get(2))

