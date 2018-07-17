import Email.Sender.Sender as Sender
import Email.Receiver.Receiver as Receiver
import time
from datetime import datetime
from Machine import Machine


class Listener:

    def __init__(self,
                 TARGET_MACHINE=Machine()
                 THIS_MACHINE=Machine()):

        self.sender = Sender(LOGIN="project.rhineheart@gmail.com",
                             PASSWORD="Bridget6",
                             RECEIVERS=["project.rhineheart@gmail.com"])

        self.receiver = Receiver(LOGIN="project.rhineheart@gmail.com",
                                 PASSWORD="Bridget6")

        self.targetMachine = TARGET_MACHINE
        self.thisMachine = THIS_MACHINE

    def receiverAction(self):
        return receiver

    def senderAction(self):
        return sender

    def listen(self, delay=3.0, loops=-1):

        count = 0
        while not (count == loops):
            time.sleep(delay)

            searchResults = self.receiverAction().searchInbox(
                    subject=str(datetime.now())[:20])

            if (len(searchResults) > 0):
                return True

            count = count + 1

        return False


