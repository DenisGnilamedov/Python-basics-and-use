class SMS_store(object):

    def __init__(self):
        self.messages = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.messages.append((False,from_number,time_arrived,text_of_SMS))

    def message_count(self):
        return len(self.messages)


my_inbox = SMS_store()
my_inbox.add_new_arrival('01234','9:37 AM','How are you?')