import threading
import time

class PrintChar(threading.Thread):
    def __init__(self, char_to_print, times):
        super().__init__()
        self.char_to_print = char_to_print
        self.times = times

    def run(self):
        for i in range (0, self.times):
            print(self.char_to_print)
            time.sleep(0.35)

class PrintNumber(threading.Thread):
    def __init__(self, number_to_print, times):
        super().__init__()
        self.number_to_print = number_to_print
        self.times = times

    def run(self):
        for i in range (0, self.times):
            print(self.number_to_print)
            time.sleep(0.35)
         


if __name__ == '__main__':
    t1 = PrintChar('A', 50)
    t2 = PrintChar('B', 50)
    t3 = PrintNumber(5, 50)

    t1.start()
    t2.start()
    t3.start()

    print('Main thread Done!!!!!!!!!')
