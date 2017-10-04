class Call(object):
    count = 0
    def __init__(self, id, caller_name, caller_number, time, reason):
        self.id = Call.count
        Call.count += 1
        self.caller_name = caller_name
        self.caller_number = caller_number
        self.time = time
        self.reason = reason
        self.taken = False
    
    
    def display(self):
        print self.id, self.caller_name, self.caller_number,self.time, self.reason
        return self


class Call_Center(object):
    def __init__(self):
        id = 0
        self.calls_list = []
        self.queue = 0

    def called(self, Call):
        # id = 0
        self.calls_list.append((Call))
        # self.id += 1
        self.queue +=1
        return self

    def received(self):
        self.taken = True
        if self.taken == True:
            self.calls_list.pop(0)
            self.queue -= 1
        return self
    
    def display_list(self):
        print self.calls_list
        print self.queue

Call1 = Call(id, "David", "222222222", "8:00", "because")
Call2 = Call(id, "Virginia", "333333333", "8:01", "same")
Call1.display()
Call2.display()
# Call_Center1 = Call_Center()
# Call_Center1.called(Call1)
# Call_Center1.received()
# Call_Center1.display_list()

