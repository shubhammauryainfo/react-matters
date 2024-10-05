from time import sleep
import random
from collections import deque
import multiprocessing

MAX_LEN = 10
buff = deque(maxlen=MAX_LEN)

class producer:
    while True:
        if len(buff) == MAX_LEN:
            print("Producer: The buff is full, waiting...")
            sleep(10)
        buff.append(random.randint(1,9))


class consumer:
    while True:
        print("Consumer: hi")
        if len(buff) == 0:
            print("Consumer: The buff is empty, waiting...")
            sleep(10)
        buff.pop()



if __name__ == '__main__':
    multiprocessing.Process(target=producer).start().join()
    multiprocessing.Process(target=consumer).start().join()
