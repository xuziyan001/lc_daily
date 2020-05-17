import threading
from multiprocessing import Process


class Foo:
    def __init__(self):
        self.cond = threading.Condition()
        self.status = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        print(threading.current_thread().name)
        self.cond.acquire()
        if self.status != 0:
            self.cond.wait()
        printFirst()
        self.status = 1
        self.cond.notify()
        self.cond.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        print(threading.current_thread().name)
        self.cond.acquire()
        if self.status != 1:
            self.cond.wait()
        printSecond()
        self.status = 2
        self.cond.notify()
        self.cond.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        print(threading.current_thread().name)
        self.cond.acquire()
        if self.status != 2:
            self.cond.wait()
        printThird()
        self.status = 0
        self.cond.notify()
        self.cond.release()


if __name__ == '__main__':
    f = Foo()
    t1 = Process(target=f.first, args=[lambda: print("first"),])
    t2 = Process(target=f.second(lambda: print("second")))
    t3 = Process(target=f.third(lambda: print("third")))
    t = [t3, t1, t2]
    for x in t:
        x.start()
    for x in t:
        x.join()
    print('finished')
