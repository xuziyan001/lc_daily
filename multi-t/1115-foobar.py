import threading
from multiprocessing import Process


class FooBar:
    def __init__(self, n):
        self.n = n
        self.s1 = threading.Semaphore(1)
        self.s2 = threading.Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        assert threading.current_thread() is threading.main_thread()
        print('foo thread: %s started' % threading.current_thread().name)

        for i in range(self.n):
            self.s1.acquire()
            printFoo()
            self.s2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        print('bar thread: %s started' % threading.current_thread().name)
        assert threading.current_thread() is threading.main_thread()
        for i in range(self.n):
            self.s2.acquire()
            printBar()
            self.s1.release()

    def foo_call(self):
        self.foo(lambda: print('foo'))

    def bar_call(self):
        self.bar(lambda: print('bar'))


if __name__ == '__main__':
    print('main thread name: %s' % threading.current_thread().name)
    f = FooBar(5)
    t1 = Process(target=f.foo_call, name='foo')
    t1.start()
    t2 = Process(target=f.bar_call, name='bar')
    t2.start()
    t1.join()
    t2.join()

