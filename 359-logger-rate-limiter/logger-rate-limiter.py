class Logger:

    def __init__(self):
        self.timeOccurance = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if (message in self.timeOccurance) and (timestamp - self.timeOccurance[message] < 10):
            return False
        else:
            self.timeOccurance[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)