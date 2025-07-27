class Logger:

    def __init__(self):
        self.lastTime = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.lastTime and timestamp - self.lastTime[message] < 10:
            return False
        self.lastTime[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)