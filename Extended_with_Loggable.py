import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(Loggable, list):
    def append(self, elem):
        x = super(LoggableList, self).append(elem)
        self.log(elem)
        return x


x = LoggableList([1, 2, 3])

print(x)
x.append(6)

x.append(6)
