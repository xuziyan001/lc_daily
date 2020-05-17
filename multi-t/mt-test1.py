# coding=utf-8
import sys
from threading import Lock, Thread

# str = input()
# print(str)
l1 = Lock()
l3 = Lock()
l5 = Lock()
l15 = Lock()


def print3():
    while True:
        l3.acquire()
        print("three")
        l1.release()


def print5():
    while True:
        l5.acquire()
        print("five")
        l1.release()


def print15():
    while True:
        l15.acquire()
        print("three_five")
        l1.release()


if __name__ == '__main__':
    n = 100
    l3.acquire()
    l5.acquire()
    l15.acquire()
    t3 = Thread(target=print3).start()
    print("test thread 3 start lock")
    t5 = Thread(target=print5).start()
    print("test thread 5 start lock")
    t15 = Thread(target=print15).start()
    print("test thread 15 start lock")
    for i in range(1, 101):
        l1.acquire()
        if i % 15 == 0:
            l15.release()
        elif i % 3 == 0:
            l3.release()
        elif i % 5 == 0:
            l5.release()
        else:
            print(i)
            l1.release()
    t3.join()
    t5.join()
    t15.join()
    l3.release()
    l5.release()
    l15.release()
