from threading import *


class flightReservation:
    l = Lock()
    def __init__(self,ticket_left):
        self.ticket_left = ticket_left

    l.acquire()

    def buy(self,ticketRequested):
        if(self.ticket_left>=ticketRequested):
            print("Your Ticket is confirmed")
            print("Please make a Payment and take your ticket")
            self.ticket_left-=ticketRequested
        else:
            print("There is not enough tickets Remaining")
    l.release()
myobj = flightReservation(10)
t1 = Thread(target=myobj.buy, args=[3])
t2 = Thread(target=myobj.buy, args=[4])
t3 = Thread(target=myobj.buy, args=[3])

t1.start()
t2.start()
t3.start()
