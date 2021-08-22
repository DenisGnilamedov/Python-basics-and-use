import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, smthg):
        elem = super(LoggableList, self).append(smthg), super(LoggableList, self).log(smthg)





a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)



# ИЛИ

class LoggableList(list, Loggable):
    def append(self, x):
        list.append(self, x)
        self.log(x)