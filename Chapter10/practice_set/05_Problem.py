# Q5)Write a class Train which has methods to book a ticket, get status (number of seats), and get fare information of a train running under Indian Railways

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to ):
        print(f"Ticket is bppked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no:{self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")            


t = Train(23456)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")