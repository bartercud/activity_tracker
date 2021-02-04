import datetime as dt

class data():
    def __init__(self, name, quantity, type, day = None):
        if (day == None):
            self.day = dt.date.today()
        else:
            self.day = day

        self.name = name
        self.quantity = quantity
        self.type = type
