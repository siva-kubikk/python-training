'''
The exercise will be to build a simple chat system where users can send and receive messages.
'''
import datetime
class Message:
    def __init__(self,sender,recipient,message) -> None:
        self.sender = sender
        self.recipient = recipient
        self.message = message
        self.timestamp = datetime.datetime.now()

class User:
    def __init__(self,username) -> None:
        self.username = username
        self.messages=[]
    
    def receive(self,message):
        self.messages.append(message)

    def send(self,recipient,message):
        message = Message(self.username, recipient.username, message)
        recipient.receive(message)

    def display(self):
        for message in self.messages:
            print(f"{message.timestamp} From: {message.sender} To: {message.recipient}, Message: {message.message}")


u1 = User('Siva')
u2 = User('Sunita')
u1.send(u2,'Hello')
u1.send(u2,'How are you?')
u1.send(u2,'I am planning to stop over.')


u2.send(u1,'I am good too.')

u1.display()
u2.display()
