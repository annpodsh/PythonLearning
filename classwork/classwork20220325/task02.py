from multiprocessing import Pool, freeze_support
import time
import struct
import random
import hashlib


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


if __name__ == '__main__':
    with Pool() as p:
        print(sum(p.map(slow_calculate, range(501))))
